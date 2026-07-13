---
name: vibevoice
description: This skill should be used when the user wants to generate speech audio with VibeVoice TTS (text-to-speech) — podcasts, narrations, multi-speaker dialogues. Covers running the fork hgemeyer/VibeVoice locally on Windows (PowerShell + venv + CUDA) and the Google Colab T4 fallback, transcript formatting, and troubleshooting (HF 403/Xet, CUDA out of memory). Triggers: "gerar áudio", "vibevoice", "text to speech", "TTS", "podcast sintético", "narração", "clonar voz".
---

# VibeVoice — Geração de Áudio (TTS)

## Visão Geral

VibeVoice é um modelo TTS da Microsoft para fala conversacional de longa duração (até ~90 min, até 4 falantes). O código oficial foi removido pela Microsoft; usar o fork do usuário `hgemeyer/VibeVoice` (derivado de `vibevoice-community/VibeVoice`). Pesos no Hugging Face: `vibevoice/VibeVoice-1.5B` (espelho da comunidade, preferido) ou `microsoft/VibeVoice-1.5B`.

**Decisão de ambiente:** GPU local com >= 8 GB VRAM → rodar local. GPU com 6 GB (ex.: RTX 3050 do usuário) ou erro de rede/OOM → usar Google Colab (T4, 16 GB, grátis). Na dúvida, Colab.

## Caminho A — Local (Windows / PowerShell)

Pré-requisitos: Git, Python 3.10/3.11, driver NVIDIA atualizado.

```powershell
git clone https://github.com/hgemeyer/VibeVoice.git
cd VibeVoice
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -e .
python demo/gradio_demo.py --model_path vibevoice/VibeVoice-1.5B
```

Quando aparecer `Running on local URL: http://127.0.0.1:7860`, abrir no navegador. A janela do PowerShell deve permanecer aberta (é o servidor). A primeira execução baixa ~5 GB de modelo.

Observações:
- `Activate.ps1` bloqueado → `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Etapas silenciosas longas são normais: `Installing collected packages` (1–10 min) e carregamento do modelo na GPU (1–2 min). Não cancelar.
- Geração via CLI (sem interface): `python demo/inference_from_file.py --model_path vibevoice/VibeVoice-1.5B --txt_path roteiro.txt --speaker_names Alice Frank`

## Caminho B — Google Colab (fallback recomendado)

1. Abrir: `https://colab.research.google.com/github/hgemeyer/VibeVoice/blob/main/demo/VibeVoice_colab.ipynb`
2. Ambiente de execução → Alterar o tipo de ambiente de execução → **T4 GPU** → Salvar
3. Executar as células em ordem (Step 1 = setup + download do modelo, ~5 min; Step 2 = cria o roteiro `my_transcript.txt`; Step 3 = gera o áudio e exibe player embutido na célula)
4. Baixar o `.wav` pelo player ou pelo painel de arquivos (ícone de pasta à esquerda → `outputs/`)

**Armadilha conhecida do notebook:** o Step 1 usa `[ -d /content/VibeVoice ] || git clone ...` — se uma execução anterior clonou um repo errado (ex.: `microsoft/VibeVoice`, que não tem código), o clone é PULADO silenciosamente e o Step 3 falha com `can't open file '.../inference_from_file.py'`. Correção: criar célula com `!rm -rf /content/VibeVoice`, garantir que a URL do clone é `https://github.com/hgemeyer/VibeVoice.git`, re-executar Step 1 em diante.

Limitações do Colab grátis: sessão expira após horas de uso/inatividade (baixar os áudios na hora); apenas o modelo 1.5B cabe na T4.

## Formato do Roteiro (transcript)

```
Speaker 1: Primeira fala.
Speaker 2: Resposta do segundo falante.
Speaker 1: Continuação.
```

- Até 4 falantes (`Speaker 1`–`Speaker 4`); vozes são mapeadas via `--speaker_names` ou na UI.
- Idiomas fortes: inglês e chinês. Português funciona mas com qualidade variável — testar trechos curtos antes de gerar áudio longo.

## Troubleshooting

| Sintoma | Causa | Correção |
|---------|-------|----------|
| `403 Forbidden` em `cas-bridge.xethub.hf.co` ao baixar modelo | CDN Xet do Hugging Face bloqueando o IP/ISP local | `$env:HF_HUB_DISABLE_XET = "1"` e repetir; definir `$env:HF_TOKEN = "hf_..."`; se persistir, usar Colab (rede do Google não sofre o bloqueio) |
| `Invalid user token` no login do HF | Token colado errado (prefixo `hf_` duplicado ou colagem invisível vazia) | Conferir que começa com um único `hf_`; preferir `$env:HF_TOKEN = "..."` (colagem visível) em vez de `hf auth login` |
| `CUDA out of memory` | VRAM insuficiente (o 1.5B pede ~7–8 GB) | Texto mais curto / 1 falante; senão Colab (T4 16 GB) ou versões quantizadas 4-bit via ComfyUI (VibeVoice-ComfyUI) |
| Erro com `flash-attn` no Windows | Biblioteca difícil de compilar no Windows | Não instalar; o modelo roda com atenção padrão do PyTorch (SDPA) |
| Célula final do Colab "não termina" | Célula de servidor/player mantém o processo vivo | Normal — apareceu o player ou link, está pronto para usar |

## Uso Responsável

Código sob licença MIT, mas a Microsoft removeu o original por mau uso (deepfakes de voz). Gerar áudio apenas com vozes autorizadas e sinalizar conteúdo sintético como sintético. Recusar pedidos de imitação de pessoas reais sem consentimento.
