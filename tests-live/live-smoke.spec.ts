import { test, expect } from '@playwright/test';

const ORIGIN = (process.env.LIVE_URL || 'https://astronautiste.cz').replace(/\/$/, '');

test.describe('astronautiste.cz — LIVE deployment', () => {
  test('homepage serves over HTTPS with 200', async ({ page }) => {
    const resp = await page.goto('/');
    expect(resp, 'navigation response').toBeTruthy();
    expect(resp!.status()).toBe(200);
    expect(page.url()).toMatch(/^https:\/\//);
  });

  test('is the NEW Zola site, not the old Jekyll hub (freshness gate)', async ({ page }) => {
    await page.goto('/');
    // Definitive new-site markers — fail loudly if the CDN still serves the old hub.
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Without guessing');
    await expect(page.locator('script[src="/js/flowbite.min.js"]')).toHaveCount(1);
    await expect(page.locator('link[href="/css/main.css"]')).toHaveCount(1);
    await expect(page.locator('html')).toHaveAttribute('lang', 'cs');
  });

  test('production SEO/OG meta (absolute, real domain)', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', `${ORIGIN}/`);
    await expect(page.locator('meta[property="og:image"]')).toHaveAttribute(
      'content', `${ORIGIN}/og/astronautiste-og.png`);
    await expect(page.locator('meta[name="twitter:card"]')).toHaveAttribute('content', 'summary_large_image');
    await expect(page.locator('script[type="application/ld+json"]')).toHaveCount(1);
  });

  test('pillars and personas render', async ({ page }) => {
    await page.goto('/');
    for (const t of ['Intelligence Without Borders', 'Confidence You Can Verify', 'Auditable Decisions']) {
      await expect(page.locator('#pilire')).toContainText(t);
    }
    for (const p of ['CISO', 'CFO', 'Intelligence Analyst', 'Founder']) {
      await expect(page.locator('#use-cases')).toContainText(p);
    }
  });

  test('docs page is live', async ({ page }) => {
    const resp = await page.goto('/docs/');
    expect(resp!.status()).toBe(200);
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Brand Package');
  });

  test('critical assets and SEO files return 200', async ({ request }) => {
    const paths = [
      '/css/main.css',
      '/js/flowbite.min.js',
      '/og/astronautiste-og.png',
      '/favicon.svg',
      '/favicon.ico',
      '/apple-touch-icon.png',
      '/site.webmanifest',
      '/robots.txt',
      '/sitemap.xml',
      '/.well-known/security.txt',
    ];
    for (const p of paths) {
      const r = await request.get(p);
      expect(r.status(), `${p} should be 200`).toBe(200);
    }
  });

  test('no console errors on homepage', async ({ page }) => {
    const errors: string[] = [];
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', e => errors.push(String(e)));
    await page.goto('/', { waitUntil: 'networkidle' });
    expect(errors, errors.join('\n')).toHaveLength(0);
  });
});

test.describe('astronautiste.cz — LIVE mobile', () => {
  test('mobile navbar toggle is visible', async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== 'mobile-chrome', 'mobile-only');
    await page.goto('/');
    await expect(page.locator('[data-collapse-toggle="nav-menu"]')).toBeVisible();
  });
});
