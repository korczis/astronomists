import { test, expect } from '@playwright/test';

test.describe('Galerie — Flowbite carousel background', () => {
  test('renders hero, tagline and CTAs', async ({ page }) => {
    await page.goto('/galerie/');
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Kampaň v pohybu');
    await expect(page.locator('section')).toContainText('Myslíme na hvězdy, jednáme vědecky');
    await expect(page.getByRole('link', { name: /Celá kampaň/i })).toBeVisible();
  });

  test('carousel has 17 poster slides + indicators + prev/next', async ({ page }) => {
    await page.goto('/galerie/');
    await expect(page.locator('[data-carousel-item]')).toHaveCount(17);
    await expect(page.locator('[data-carousel-slide-to]')).toHaveCount(17);
    await expect(page.locator('[data-carousel-prev]')).toBeVisible();
    await expect(page.locator('[data-carousel-next]')).toBeVisible();
  });

  test('Flowbite initialises — exactly one slide in viewport', async ({ page }) => {
    await page.goto('/galerie/');
    // Flowbite "slide" keeps a 3-item window un-hidden but translates the
    // prev/next off-screen, so exactly one item intersects the viewport.
    await expect.poll(async () =>
      page.locator('[data-carousel-item]').evaluateAll((els) => {
        const vw = window.innerWidth, vh = window.innerHeight;
        return els.filter((e) => {
          const r = e.getBoundingClientRect();
          return r.width > 0 && r.height > 0 && r.left < vw && r.right > 0 && r.top < vh && r.bottom > 0;
        }).length;
      })
    , { timeout: 5000 }).toBe(1);
    await expect(page.locator('[data-carousel-item] img').first()).toHaveAttribute('alt', /.+/);
  });
});
