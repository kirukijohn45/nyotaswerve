import type { Metadata } from 'next';
export const metadata: Metadata = { title: 'Nyota Swerve', description: 'Luxury Bespoke Tailoring' };
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body className="bg-[#0D0D0D] text-white">{children}</body></html>;
}
