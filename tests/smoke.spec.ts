import { test, expect } from '@playwright/test';

test.describe('Astronautisté landing — smoke', () => {
  test('homepage loads with brand title and hero', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Astronautisté/);
    await expect(page.locator('html')).toHaveAttribute('lang', 'cs');
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Without guessing');
  });

  test('hero CTAs and nav present', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('link', { name: /Launch your investigation/i })).toBeVisible();
    await expect(page.locator('nav')).toContainText('ASTRONAUTISTÉ');
  });

  test('three product pillars render', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#pilire')).toContainText('Intelligence Without Borders');
    await expect(page.locator('#pilire')).toContainText('Confidence You Can Verify');
    await expect(page.locator('#pilire')).toContainText('Auditable Decisions');
  });

  test('use-cases cover the four personas', async ({ page }) => {
    await page.goto('/');
    const uc = page.locator('#use-cases');
    for (const persona of ['CISO', 'CFO', 'Intelligence Analyst', 'Founder']) {
      await expect(uc).toContainText(persona);
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
