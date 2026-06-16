import { defineConfig, devices } from '@playwright/test';

// Live smoke against the deployed site. No local webServer — hits the real CDN.
// Override target with LIVE_URL=... (default: production domain).
const BASE = process.env.LIVE_URL || 'https://astronautiste.cz';

export default defineConfig({
  testDir: './tests-live',
  timeout: 45_000,
  expect: { timeout: 15_000 },
  fullyParallel: true,
  retries: 2, // CDN / propagation flakiness
  reporter: process.env.CI ? [['github'], ['list']] : 'list',
  use: {
    baseURL: BASE,
    navigationTimeout: 30_000,
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
  ],
});
