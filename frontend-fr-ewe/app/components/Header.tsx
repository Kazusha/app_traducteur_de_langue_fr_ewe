export default function Header() {
  return (
    <header className="bg-gray-50 shadow-md sticky top-0 z-50 px-5 py-6 w-full text-green-600 flex justify-between items-center">
      <h1 className="font-orbitron text-2xl tracking-wide cursor-pointer">LimanTrad</h1>
      <a href="https://huggingface.co/liman21/nllb-fr-ewe-midjie21" target="_blank" rel="noopener noreferrer">
        <img src="/images-removebg-preview.png" alt="LimanTrad Logo" className="h-16 w-32" />
      </a>
    </header>
  );
}