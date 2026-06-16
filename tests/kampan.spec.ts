import { test, expect } from '@playwright/test';

// E2E coverage for the campaign build-out: the /kampan/ hub, its 25 detail pages,
// the prev/next chain, and the /docs/social-kit/ gallery. Complements pages.spec.ts
// (which checks representative routes) by exercising the full series + leaf behaviours.

const HUB = '/kampan/';
const FIRST = '/kampan/01-zvedavost-je-start/';
const MIDDLE = '/kampan/13-vesmir-neni-luxus/';
const LAST = '/kampan/25-zacni-otazkou/';

// Per-page OG override points at the series-25 social preview, not the site default.
const SERIES_OG = /\/og\/social\/series-25-20260616\/astronautiste-\d{2}-.+-social\.jpg$/;

async function cardHrefs(page: import('@playwright/test').Page): Promise<string[]> {
  await page.goto(HUB);
  return page.locator('main a[href^="/kampan/"]').evaluateAll(
    els => [...new Set(els
      .map(e => (e as HTMLAnchorElement).getAttribute('href')!)
      .filter(h => h !== '/kampan/'))]);
}

test.describe('kampaň hub', () => {
  test('hub lists exactly 25 detail cards, each with a thumbnail', async ({ page }) => {
    const hrefs = await cardHrefs(page);
    expect(hrefs.length, 'hub lists 25 cards').toBe(25);

    // Each card carries an OG/thumb image (series-25 preview).
    const imgs = page.locator('main a[href^="/kampan/"] img');
    expect(await imgs.count(), 'cards have images').toBeGreaterThanOrEqual(25);
    await expect(imgs.first()).toHaveAttribute('src', SERIES_OG);
  });

  test('hub heading + eyebrow render', async ({ page }) => {
    await page.goto(HUB);
    await expect(page.getByRole('heading', { level: 1 })).toContainText('25 plakátů');
    await expect(page.locator('main')).toContainText('Kampaň 2026');
  });
});

test.describe('kampaň detail pages', () => {
  test('all 25 details resolve with a unique title and series-25 og:image', async ({ page }) => {
    const hrefs = await cardHrefs(page);
    const titles = new Set<string>();
    const ogs = new Set<string>();

    for (const href of hrefs) {
      const resp = await page.goto(href);
      expect(resp!.status(), `${href} status`).toBe(200);

      const title = await page.title();
      expect(titles.has(title), `${href} unique title "${title}"`).toBeFalsy();
      titles.add(title);

      const og = await page.locator('meta[property="og:image"]').getAttribute('content');
      expect(og, `${href} og:image is its series-25 preview`).toMatch(SERIES_OG);
      ogs.add(og!);

      await expect(page.getByRole('heading', { level: 1 }), `${href} H1`).toBeVisible();
    }

    expect(ogs.size, 'every detail has a distinct og:image').toBe(25);
  });

  test('detail renders eyebrow, lead, anchor quote, hero image and breadcrumb', async ({ page }) => {
    await page.goto(MIDDLE);
    // Eyebrow (accent) + lead (subhead)
    await expect(page.locator('.eyebrow')).toContainText('PERSPEKTIVA');
    await expect(page.locator('main')).toContainText('kterou si zaslouží každý');
    // Anchor blockquote (proof)
    await expect(page.locator('article blockquote')).toContainText('návrat k Zemi');
    // Hero background image (from extra.image)
    await expect(page.locator('article img[class*="object-cover"]').first()).toBeVisible();
    // Breadcrumb back to hub + home
    const crumb = page.locator('nav[aria-label="Drobečková navigace"]');
    await expect(crumb.locator('a[href="/kampan/"]')).toBeVisible();
    await expect(crumb.locator('a[href="/"]')).toBeVisible();
  });
});

test.describe('kampaň prev/next chain', () => {
  const nextLink = (page: import('@playwright/test').Page) =>
    page.locator('nav[aria-label="Další v sekci"] a').filter({ hasText: 'Další' });
  const prevLink = (page: import('@playwright/test').Page) =>
    page.locator('nav[aria-label="Další v sekci"] a').filter({ hasText: 'Předchozí' });

  test('first page has next but no previous', async ({ page }) => {
    await page.goto(FIRST);
    await expect(nextLink(page)).toHaveCount(1);
    await expect(prevLink(page)).toHaveCount(0);
  });

  test('last page has previous but no next', async ({ page }) => {
    await page.goto(LAST);
    await expect(prevLink(page)).toHaveCount(1);
    await expect(nextLink(page)).toHaveCount(0);
  });

  test('middle page links both ways and "Další" advances within /kampan/', async ({ page }) => {
    await page.goto(MIDDLE);
    await expect(prevLink(page)).toHaveCount(1);
    await expect(nextLink(page)).toHaveCount(1);

    await nextLink(page).click();
    await expect(page).toHaveURL(/\/kampan\/\d{2}-.+\//);
    expect(page.url(), 'advanced to a different detail').not.toContain('13-vesmir-neni-luxus');
    await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
  });
});

test.describe('social / OG kit gallery', () => {
  test('gallery resolves with stats, preview figures and brand-QA table', async ({ page }) => {
    const resp = await page.goto('/docs/social-kit/');
    expect(resp!.status(), 'social-kit status').toBe(200);
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Náhledy pro sdílení');

    // Stat chips render numeric counts from data/og-previews.toml.
    const total = await page.locator('dl dd').first().textContent();
    expect(Number(total?.trim()), 'total previews > 0').toBeGreaterThan(0);

    // Preview images load from /og/ and the default hero is shown.
    const previews = page.locator('figure img');
    expect(await previews.count(), 'gallery has previews').toBeGreaterThan(5);
    await expect(previews.first()).toHaveAttribute('src', /\/og\/.+\.(jpg|jpeg|png|webp)$/);

    // Brand QA correction table is present.
    await expect(page.locator('table')).toContainText('ASTRONAUTISTÉ');
  });
});
