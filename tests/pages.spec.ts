import { test, expect } from '@playwright/test';

// Representative route per page-type (hubs + leaves + kampaň). Every route must be
// bookmarkable: 200, unique <title>, absolute canonical + og:image, full social meta.
const ROUTES = [
  '/',
  '/proc/', '/proc/perspektiva/', '/proc/zvidavost/', '/proc/budoucnost/',
  '/manifest/', '/manifest/detem-patri-hvezdy/', '/manifest/ne-vetsi-stat/',
  '/pro-koho/', '/pro-koho/rodice/', '/pro-koho/vedci/',
  '/motivy/', '/motivy/pale-blue-dot/', '/motivy/nejnebezpecnejsi-poster/',
  '/pridej-se/', '/pridej-se/skolni-vylet-orbit/',
  '/brand/', '/docs/',
  '/kampan/', '/kampan/01-zvedavost-je-start/',
];

const ABS_IMG = /^https?:\/\/[^/]+\/.+\.(png|jpg|jpeg|webp)$/;

test.describe('per-page SEO / OG / social meta', () => {
  test('every route is bookmarkable with complete, unique meta', async ({ page }) => {
    const titles = new Set<string>();
    const ogImages = new Set<string>();

    for (const route of ROUTES) {
      const resp = await page.goto(route);
      expect(resp, `${route} response`).toBeTruthy();
      expect(resp!.status(), `${route} status`).toBe(200);

      // Unique <title>
      const title = await page.title();
      expect(title.length, `${route} has title`).toBeGreaterThan(3);
      expect(titles.has(title), `${route} title unique: "${title}"`).toBeFalsy();
      titles.add(title);

      // Description present
      await expect(page.locator('meta[name="description"]'), route).toHaveCount(1);

      // Canonical absolute + exactly one
      const canonical = await page.locator('link[rel="canonical"]').getAttribute('href');
      expect(canonical, `${route} canonical absolute`).toMatch(/^https?:\/\//);

      // OG + Twitter
      const og = await page.locator('meta[property="og:image"]').getAttribute('content');
      expect(og, `${route} og:image absolute`).toMatch(ABS_IMG);
      ogImages.add(og!);
      await expect(page.locator('meta[property="og:title"]'), route).toHaveCount(1);
      await expect(page.locator('meta[property="og:url"]'), route).toHaveCount(1);
      await expect(page.locator('meta[name="twitter:card"]'), route)
        .toHaveAttribute('content', 'summary_large_image');
      await expect(page.locator('script[type="application/ld+json"]'), route).toHaveCount(1);

      // One visible H1
      await expect(page.getByRole('heading', { level: 1 }), route).toBeVisible();
    }

    // Previews are unique per page (allow a tiny overlap margin for shared defaults).
    expect(ogImages.size, 'og:image largely unique per page').toBeGreaterThanOrEqual(ROUTES.length - 2);
  });

  test('hub pages list child cards that link to detail pages', async ({ page }) => {
    await page.goto('/motivy/');
    await expect(page.locator('a[href="/motivy/pale-blue-dot/"]')).toHaveCount(1);
    await page.goto('/proc/');
    await expect(page.locator('a[href="/proc/perspektiva/"]')).toHaveCount(1);
  });

  test('detail page has breadcrumb back to its hub', async ({ page }) => {
    await page.goto('/motivy/pale-blue-dot/');
    const crumb = page.locator('nav[aria-label="Drobečková navigace"]');
    await expect(crumb.locator('a[href="/motivy/"]')).toBeVisible();
    await expect(crumb.locator('a[href="/"]')).toBeVisible();
  });

  test('every top-navbar link resolves (200 + visible H1)', async ({ page }) => {
    await page.goto('/');
    const hrefs = await page.locator('nav[aria-label="Hlavní navigace"] a[href^="/"]')
      .evaluateAll(els => [...new Set(els.map(e => (e as HTMLAnchorElement).getAttribute('href')!))]);
    expect(hrefs.length, 'navbar has links').toBeGreaterThanOrEqual(7);
    for (const h of hrefs) {
      const r = await page.goto(h);
      expect(r!.status(), `navbar ${h} status`).toBe(200);
      await expect(page.getByRole('heading', { level: 1 }), `navbar ${h} H1`).toBeVisible();
    }
  });

  test('hub card images are uniform 16:10, object-cover, sized (no stretch / no CLS)', async ({ page }) => {
    await page.goto('/motivy/');
    const imgs = page.locator('main section a[href^="/motivy/"] img');
    const n = await imgs.count();
    expect(n, 'motif cards present').toBeGreaterThanOrEqual(10);
    for (let i = 0; i < n; i++) {
      const im = imgs.nth(i);
      await expect(im, `card img ${i} width`).toHaveAttribute('width', '1280');
      await expect(im, `card img ${i} height`).toHaveAttribute('height', '800');
      expect(await im.getAttribute('class'), `card img ${i} object-cover`).toContain('object-cover');
      const box = await im.boundingBox();
      expect(box, `card img ${i} box`).toBeTruthy();
      // rendered ratio must be ~16:10 (1.6) — proves no stretch/letterbox
      expect(Math.abs(box!.width / box!.height - 1.6), `card img ${i} AR`).toBeLessThan(0.06);
    }
  });

  test('every hub card links to a page that resolves', async ({ page }) => {
    const hubs = ['/proc/', '/manifest/', '/pro-koho/', '/motivy/', '/pridej-se/', '/kampan/'];
    for (const hub of hubs) {
      await page.goto(hub);
      const cards: string[] = await page.locator('main a[href^="/"]').evaluateAll(
        (els, hub) => [...new Set(els
          .map(e => (e as HTMLAnchorElement).getAttribute('href')!)
          .filter(h => h.startsWith(hub) && h !== hub))], hub);
      expect(cards.length, `${hub} lists child cards`).toBeGreaterThan(0);
      for (const c of cards) {
        const r = await page.goto(c);
        expect(r!.status(), `${hub} card ${c}`).toBe(200);
      }
    }
  });
});
