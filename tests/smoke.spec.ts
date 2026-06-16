import { test, expect } from '@playwright/test';

test.describe('Astronautisté landing — smoke', () => {
  test('homepage loads with brand title and hero', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Astronautisté/);
    await expect(page.locator('html')).toHaveAttribute('lang', 'cs');
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Dětem patří hvězdy');
  });

  test('hero CTAs and nav present', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('link', { name: /Přidej se/i }).first()).toBeVisible();
    await expect(page.locator('nav')).toContainText('ASTRONAUTISTÉ');
  });

  test('three movement pillars render', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#proc')).toContainText('Perspektiva');
    await expect(page.locator('#proc')).toContainText('Zvídavost');
    await expect(page.locator('#proc')).toContainText('Budoucnost');
  });

  test('audiences cover the four groups', async ({ page }) => {
    await page.goto('/');
    const uc = page.locator('#pro-koho');
    for (const aud of ['Rodiče', 'Učitelé', 'Studenti', 'Vědci']) {
      await expect(uc).toContainText(aud);
    }
  });

  test('SEO/OG meta present and absolute', async ({ page }) => {
    await page.goto('/');
    // absolute URL (scheme + host) ending in the OG image path — host varies by build base_url
    await expect(page.locator('meta[property="og:image"]')).toHaveAttribute(
      'content', /^https?:\/\/[^/]+\/og\/astronautiste-og\.png$/);
    await expect(page.locator('meta[name="twitter:card"]')).toHaveAttribute('content', 'summary_large_image');
    await expect(page.locator('link[rel="canonical"]')).toHaveCount(1);
    await expect(page.locator('script[type="application/ld+json"]')).toHaveCount(1);
  });

  test('docs page resolves', async ({ page }) => {
    await page.goto('/docs/');
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Brand Package');
    await expect(page.getByRole('link').first()).toBeVisible();
  });

  test('enhancement layer is wired and vendored locally (no external CDN scripts)', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#starfield-host')).toHaveCount(1);
    for (const src of ['/js/p5.min.js', '/js/alpine.min.js', '/js/alpine-intersect.min.js', '/js/flowbite.min.js']) {
      await expect(page.locator(`script[src="${src}"]`)).toHaveCount(1);
    }
    // Libraries are vendored — no third-party <script src="http...">.
    await expect(page.locator('script[src^="http"]')).toHaveCount(0);
  });

  test('p5 starfield canvas renders in the hero', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#starfield-host canvas')).toBeVisible();
  });

  test('scroll-reveal sections become visible (Alpine x-intersect)', async ({ page }) => {
    await page.goto('/');
    const brand = page.locator('#brand');
    await brand.scrollIntoViewIfNeeded();
    await expect(brand).toHaveClass(/is-in/);
    await expect(brand).toBeVisible();
  });

  test('no internal anchor targets are missing', async ({ page }) => {
    await page.goto('/');
    const hrefs = await page.locator('a[href^="#"]').evaluateAll(
      els => els.map(e => (e as HTMLAnchorElement).getAttribute('href')!).filter(h => h.length > 1));
    for (const h of new Set(hrefs)) {
      await expect(page.locator(h), `anchor ${h} should exist`).toHaveCount(1);
    }
  });
});

test.describe('responsive — mobile', () => {
  test('mobile navbar toggle is visible', async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== 'mobile-chrome', 'mobile-only');
    await page.goto('/');
    await expect(page.locator('[data-collapse-toggle="nav-menu"]')).toBeVisible();
  });
});
