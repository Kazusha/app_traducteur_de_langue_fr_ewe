import type { TranslationResponse } from "./type";

export async function translateText(text: string): Promise<TranslationResponse>{
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/translate`,{
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({ text }),
    });

    if (!response.ok){
        throw new Error(`Erreur ${response.status}`);
    }

    return response.json()
}
   