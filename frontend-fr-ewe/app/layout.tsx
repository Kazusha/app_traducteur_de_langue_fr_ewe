import type { Metadata } from "next";
import { Orbitron } from "next/font/google";
import Header from "./components/Header"
import "./globals.css";


const orbitron = Orbitron({
  variable: "--font-orbitron",
  subsets: ["latin"],
})
export const metadata: Metadata = {
  title: "LimanTrad",
  description: "Traduction Francais vers ewe",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${orbitron.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col"><Header />{children}</body>
    </html>
  );
}
