import { defineConfig, devices } from '@playwright/test';

const PORT = 8799;
const BASE = `http://localhost:${PORT}`;

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  expect: { timeout: 10_000 },
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  reporter: process.env.CI ? [['github'], ['list']] : 'list',
  use: {
    baseURL: BASE,
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
  ],
  webServer: {
    // Full pipeline (Tailwind/Flowbite + Zola) into public-test, then serve it.
    command: `BASE_URL=${BASE} OUTPUT_DIR=public-test bash scripts/build.sh && python3 -m http.server ${PORT} --directory public-test`,
    port: PORT,
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
});
