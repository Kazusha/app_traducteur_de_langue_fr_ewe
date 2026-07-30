"use client";

import { useState , useEffect } from "react";
import { translateText } from "@/lib/api";
import Swal from "sweetalert2";





export default function Home() {
 const [sourceText , setSourceText] = useState("");
 const [translatedText , setTranslatedText] = useState("");
 const [isLoading , setIsLoading] = useState(false)

 useEffect(() => {
  Swal.fire({
    icon: "info",
    title: "Bienvenue sur LimanTrad",
    html: `
      <p>Écris ton texte en français dans le champ, puis clique sur "Traduire" pour obtenir sa traduction en ewe.</p>
    `,
    confirmButtonText: "C'est parti",
  });
}, []);

 const handleTranslate = async () => {
  if (!sourceText.trim()) return;
  setIsLoading(true);
  try{
    const result = await translateText(sourceText);
    setTranslatedText(result.translated_text);
  }catch (err){
    const message= 
      err instanceof Error && err.message.includes("429")
      ? "Trop de requetes effectuees. Attendez un instant avant de ressayer"
      : "Une erreur est survenue pendant la traduction. Reessaie";

      Swal.fire({
        icon : "error",
        title: "Oups",
        text: message,
      });

  }finally {
    setIsLoading(false);
  }

 };

  return (
    <main className="bg-gray-50 flex-1 flex flex-col gap-6 px-6 py-10 items-center">
          <div className="w-full max-w-4xl flex flex-col md:flex-row items-stretch gap-4">

      <div className=" flex flex-1 flex-col gap-2">
        <label htmlFor="source" className="text-sm text-green-500 ">
          Français
        </label>
        <textarea id="source" value={sourceText} onChange={(e) => setSourceText(e.target.value)} rows={8} className="border rounded p-3 resize-none  text-black font-semibold" placeholder="Ecris ton texte en francais" />

      </div>
      <div className =" flex items-center justify-center">
              <button onClick={handleTranslate} disabled={isLoading || !sourceText.trim()} className="px-6 py-2 rounded bg-green-500 text-white disabled:opacity-50">
        {isLoading ? "Traduction":"Traduire"}
      </button>
      </div>


      <div className="flex flex-1 flex-col gap-2">
        <label htmlFor="target" className="text-sm text-green-500">
          Ewe
        </label>
 <textarea
    id="target"
    value={translatedText}
    readOnly
    rows={8}
    className="border rounded-lg  p-3 resize-none  text-black font-semibold"
    placeholder="La traduction apparaîtra ici"
  />      
  </div>

    </div>
      </main>

  );
}
