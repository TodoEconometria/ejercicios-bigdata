---
hide:
  - toc
---

# Ranking de Estudiantes

<style>
.podium-card {
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: default;
}
.podium-card:hover {
  transform: translateY(-10px) scale(1.04);
}
.podium-gold:hover {
  box-shadow: 0 0 50px rgba(249,212,35,0.55), 0 10px 30px rgba(0,0,0,0.4) !important;
}
.podium-silver:hover {
  box-shadow: 0 0 50px rgba(168,180,194,0.45), 0 10px 30px rgba(0,0,0,0.4) !important;
}
.podium-bronze:hover {
  box-shadow: 0 0 50px rgba(205,127,50,0.45), 0 10px 30px rgba(0,0,0,0.4) !important;
}
.podium-card img {
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.podium-card:hover img {
  transform: scale(1.12);
}
.podium-gold:hover img {
  box-shadow: 0 0 30px rgba(249,212,35,0.7) !important;
}
.podium-silver:hover img {
  box-shadow: 0 0 30px rgba(168,180,194,0.6) !important;
}
.podium-bronze:hover img {
  box-shadow: 0 0 30px rgba(205,127,50,0.6) !important;
}
.podium-card .fork-btn {
  transition: background 0.3s ease, transform 0.3s ease;
}
.podium-card:hover .fork-btn {
  transform: scale(1.05);
}
.stat-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}
.challenger-card {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: default;
}
.challenger-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 4px 20px rgba(102,126,234,0.2), 0 2px 10px rgba(0,0,0,0.3) !important;
  border-color: rgba(102,126,234,0.25) !important;
}
.challenger-card:hover img {
  border-color: #667eea !important;
}
details > summary {
  list-style: none;
}
details > summary::-webkit-details-marker {
  display: none;
}
details[open] > summary {
  margin-bottom: 10px;
}
.logo-glow-wrap {
  display: inline-block;
  position: relative;
  margin-bottom: 12px;
}
.logo-glow-wrap img {
  display: block;
  width: 200px;
  height: auto;
  border-radius: 15px;
}
/* SVG ECG - linea de vida bajo el logo */
.ecg-svg {
  position: absolute;
  bottom: -4px;
  left: -5px;
  width: calc(100% + 10px);
  height: 32px;
  z-index: 2;
  pointer-events: none;
}
</style>

<div style="text-align: center; padding: 10px 0;">
<div class="logo-glow-wrap"><img src="../assets/todoeconometria_logo.png" alt="TodoEconometria"><svg class="ecg-svg" viewBox="-5 -2 210 32"><defs><filter id="ecg-glow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="ecg-colors" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="200" y2="0"><stop offset="0%" stop-color="#a51d4e"/><stop offset="20%" stop-color="#e63946"/><stop offset="40%" stop-color="#f4a233"/><stop offset="60%" stop-color="#2d8a56"/><stop offset="80%" stop-color="#3470bc"/><stop offset="100%" stop-color="#a51d4e"/></linearGradient></defs><path d="M -200,20 H -50 l 5,-3 l 5,3 l 5,0 l 2,3 l 2,-18 l 2,20 l 2,-5 l 5,0 l 4,-4 l 5,4 H 0 H 150 l 5,-3 l 5,3 l 5,0 l 2,3 l 2,-18 l 2,20 l 2,-5 l 5,0 l 4,-4 l 5,4 H 200 H 350 l 5,-3 l 5,3 l 5,0 l 2,3 l 2,-18 l 2,20 l 2,-5 l 5,0 l 4,-4 l 5,4 H 400" fill="none" stroke="url(#ecg-colors)" stroke-width="3" stroke-linecap="round" filter="url(#ecg-glow)" stroke-dasharray="90 642"><animate attributeName="stroke-dashoffset" from="0" to="-732" dur="3s" repeatCount="indefinite"/></path></svg></div>
<p style="font-size: 1.1em; font-style: italic; color: #888;">
Tabla de posiciones del curso Big Data con Python
</p>
<p style="color: #666; font-size: 0.9em;">
Ultima actualizacion: 2026-02-14 02:30 | Ranking actualizado semanalmente
</p>
</div>

---

<h2 style="border: none;">Estadisticas del Curso</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin: 30px 0; text-align: center;">
<div class="stat-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 20px; border: 1px solid rgba(255,255,255,0.05);"><div style="font-size: 2.5em; font-weight: 900; color: #f39c12; text-shadow: 0 0 20px rgba(243,156,18,0.3);">18</div><div style="color: #888; font-size: 0.9em; margin-top: 4px;">Estudiantes</div></div><div class="stat-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 20px; border: 1px solid rgba(255,255,255,0.05);"><div style="font-size: 2.5em; font-weight: 900; color: #2ecc71; text-shadow: 0 0 20px rgba(46,204,113,0.3);">5</div><div style="color: #888; font-size: 0.9em; margin-top: 4px;">Entregados</div></div><div class="stat-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 20px; border: 1px solid rgba(255,255,255,0.05);"><div style="font-size: 2.5em; font-weight: 900; color: #3498db; text-shadow: 0 0 20px rgba(52,152,219,0.3);">6.3</div><div style="color: #888; font-size: 0.9em; margin-top: 4px;">Promedio</div></div><div class="stat-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 20px; border: 1px solid rgba(255,255,255,0.05);"><div style="font-size: 2.5em; font-weight: 900; color: #e74c3c; text-shadow: 0 0 20px rgba(231,76,60,0.3);">2</div><div style="color: #888; font-size: 0.9em; margin-top: 4px;">Destacados</div></div>
</div>

---

<h2 style="border: none;">Leaderboard</h2>

<div style="display: grid; grid-template-columns: 1fr 1.2fr 1fr; gap: 14px; margin: 30px auto; max-width: 820px; align-items: end;">
<div class="podium-card podium-silver" style="min-height: 300px; background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%); border-radius: 16px; padding: 22px 14px 18px; border: 1px solid #a8b4c240; box-shadow: 0 0 25px rgba(168,180,194,0.2), 0 4px 15px rgba(0,0,0,0.3); display: flex; flex-direction: column; align-items: center; position: relative; overflow: hidden;"><div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #a8b4c2, transparent);"></div><div style="font-size: 1.6em; font-weight: 900; color: #c0c0c0; text-shadow: 0 0 15px rgba(168,180,194,0.2); margin-bottom: 10px; letter-spacing: 2px;">#2 <span style="font-size: 0.42em; color: #888; font-weight: 600; background: rgba(255,255,255,0.06); border-radius: 8px; padding: 1px 7px; vertical-align: middle; letter-spacing: 0;">4sem</span></div><img src="https://github.com/aurorafezu.png" alt="@aurorafezu" style="width: 72px; height: 72px; border-radius: 50%; border: 3px solid #a8b4c2; box-shadow: 0 0 15px rgba(168,180,194,0.2); object-fit: cover; background: #2a2a3a;" onerror="this.style.display='none'"><div style="margin-top: 10px; font-weight: 700; color: #eee; font-size: 0.95em;">@aurorafezu</div><div style="font-size: 2em; font-weight: 900; color: #c0c0c0; text-shadow: 0 0 10px rgba(168,180,194,0.2); margin: 4px 0; letter-spacing: 1px;">8.2</div><div style="width: 90%; margin: 10px 0 6px;"><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #e8b84b; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #1a1a2e;">D</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 70%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">7.0</span></div><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #667eea; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #fff;">C</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 100%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">10.0</span></div></div><div style="margin: 4px 0;"><span style="display: inline-block; background: rgba(46,204,113,0.15); border: 1px solid rgba(46,204,113,0.4); border-radius: 10px; padding: 2px 10px; font-size: 0.65em; color: #2ecc71;">&#10003; Puntual</span></div><div style="margin: 6px 0 4px; line-height: 1.8;"><span style="display: inline-block; background: rgba(102,126,234,0.12); border: 1px solid rgba(102,126,234,0.25); border-radius: 10px; padding: 1px 9px; font-size: 0.68em; color: #8b9cf7; margin: 1px 2px;">clustering</span><span style="display: inline-block; background: rgba(102,126,234,0.12); border: 1px solid rgba(102,126,234,0.25); border-radius: 10px; padding: 1px 9px; font-size: 0.68em; color: #8b9cf7; margin: 1px 2px;">k-means</span></div><div style="display: flex; gap: 6px; margin-top: auto; flex-wrap: wrap; justify-content: center;"><a class="fork-btn" href="https://github.com/aurorafezu/ejercicios-bigdata/tree/main/entregas/trabajo_final/fernandez_aurora" target="_blank" style="color: #c0c0c0; text-decoration: none; font-size: 0.75em; padding: 5px 14px; border: 1px solid #a8b4c250; border-radius: 20px; background: #a8b4c210;">Ver Entrega</a><a class="fork-btn" href="https://raw.githack.com/aurorafezu/ejercicios-bigdata/main/entregas/trabajo_final/fernandez_aurora/dashboard_interactivo.html" target="_blank" style="color: #2ecc71; text-decoration: none; font-size: 0.75em; padding: 5px 14px; border: 1px solid rgba(46,204,113,0.5); border-radius: 20px; background: rgba(46,204,113,0.1);">Dashboard</a></div></div><div class="podium-card podium-gold" style="min-height: 360px; background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%); border-radius: 16px; padding: 22px 14px 18px; border: 1px solid #f9d42340; box-shadow: 0 0 25px rgba(249,212,35,0.3), 0 4px 15px rgba(0,0,0,0.3); display: flex; flex-direction: column; align-items: center; position: relative; overflow: hidden;"><div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #f9d423, transparent);"></div><div style="font-size: 1.6em; font-weight: 900; color: #f9d423; text-shadow: 0 0 15px rgba(249,212,35,0.3); margin-bottom: 10px; letter-spacing: 2px;">#1 <span style="font-size: 0.42em; color: #888; font-weight: 600; background: rgba(255,255,255,0.06); border-radius: 8px; padding: 1px 7px; vertical-align: middle; letter-spacing: 0;">4sem</span></div><img src="https://github.com/katitto.png" alt="@katitto" style="width: 90px; height: 90px; border-radius: 50%; border: 3px solid #f9d423; box-shadow: 0 0 15px rgba(249,212,35,0.3); object-fit: cover; background: #2a2a3a;" onerror="this.style.display='none'"><div style="margin-top: 10px; font-weight: 700; color: #eee; font-size: 0.95em;">@katitto</div><div style="font-size: 2.6em; font-weight: 900; color: #f9d423; text-shadow: 0 0 10px rgba(249,212,35,0.3); margin: 4px 0; letter-spacing: 1px;">8.7</div><div style="width: 90%; margin: 10px 0 6px;"><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #e8b84b; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #1a1a2e;">D</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 95%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">9.5</span></div><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #667eea; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #fff;">C</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 100%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">10.0</span></div></div><div style="margin: 4px 0;"><span style="display: inline-block; background: rgba(46,204,113,0.15); border: 1px solid rgba(46,204,113,0.4); border-radius: 10px; padding: 2px 10px; font-size: 0.65em; color: #2ecc71;">&#10003; Puntual</span></div><div style="margin: 6px 0 4px; line-height: 1.8;"><span style="display: inline-block; background: rgba(102,126,234,0.12); border: 1px solid rgba(102,126,234,0.25); border-radius: 10px; padding: 1px 9px; font-size: 0.68em; color: #8b9cf7; margin: 1px 2px;">pca</span><span style="display: inline-block; background: rgba(102,126,234,0.12); border: 1px solid rgba(102,126,234,0.25); border-radius: 10px; padding: 1px 9px; font-size: 0.68em; color: #8b9cf7; margin: 1px 2px;">time series</span></div><div style="display: flex; gap: 6px; margin-top: auto; flex-wrap: wrap; justify-content: center;"><a class="fork-btn" href="https://github.com/katitto/ejercicios-bigdata/tree/main/entregas/trabajo_final/almache_katherine" target="_blank" style="color: #f9d423; text-decoration: none; font-size: 0.75em; padding: 5px 14px; border: 1px solid #f9d42350; border-radius: 20px; background: #f9d42310;">Ver Entrega</a><a class="fork-btn" href="https://raw.githack.com/katitto/ejercicios-bigdata/main/entregas/trabajo_final/almache_katherine/outputs/dashboard/index.html" target="_blank" style="color: #2ecc71; text-decoration: none; font-size: 0.75em; padding: 5px 14px; border: 1px solid rgba(46,204,113,0.5); border-radius: 20px; background: rgba(46,204,113,0.1);">Dashboard</a></div></div><div class="podium-card podium-bronze" style="min-height: 280px; background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%); border-radius: 16px; padding: 22px 14px 18px; border: 1px solid #cd7f3240; box-shadow: 0 0 25px rgba(205,127,50,0.2), 0 4px 15px rgba(0,0,0,0.3); display: flex; flex-direction: column; align-items: center; position: relative; overflow: hidden;"><div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #cd7f32, transparent);"></div><div style="font-size: 1.6em; font-weight: 900; color: #cd7f32; text-shadow: 0 0 15px rgba(205,127,50,0.2); margin-bottom: 10px; letter-spacing: 2px;">#3 <span style="font-size: 0.42em; color: #888; font-weight: 600; background: rgba(255,255,255,0.06); border-radius: 8px; padding: 1px 7px; vertical-align: middle; letter-spacing: 0;">4sem</span></div><img src="https://github.com/luuuuru.png" alt="@luuuuru" style="width: 72px; height: 72px; border-radius: 50%; border: 3px solid #cd7f32; box-shadow: 0 0 15px rgba(205,127,50,0.2); object-fit: cover; background: #2a2a3a;" onerror="this.style.display='none'"><div style="margin-top: 10px; font-weight: 700; color: #eee; font-size: 0.95em;">@luuuuru</div><div style="font-size: 2em; font-weight: 900; color: #cd7f32; text-shadow: 0 0 10px rgba(205,127,50,0.2); margin: 4px 0; letter-spacing: 1px;">7.0</div><div style="width: 90%; margin: 10px 0 6px;"><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #e8b84b; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #1a1a2e;">D</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 0%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">0.0</span></div><div style="display: flex; align-items: center; gap: 5px; margin: 4px 0;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #667eea; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #fff;">C</span><div style="flex: 1; background: #2a2a3a; border-radius: 4px; height: 7px; overflow: hidden;"><div style="width: 100%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 4px;"></div></div><span style="font-size: 0.7em; color: #999; width: 28px; text-align: right;">10.0</span></div></div><div style="margin: 4px 0;"><span style="display: inline-block; background: rgba(46,204,113,0.15); border: 1px solid rgba(46,204,113,0.4); border-radius: 10px; padding: 2px 10px; font-size: 0.65em; color: #2ecc71;">&#10003; Puntual</span></div><div style="display: flex; gap: 6px; margin-top: auto; flex-wrap: wrap; justify-content: center;"><a class="fork-btn" href="https://github.com/luuuuru/ejercicios-bigdata/tree/main/entregas/trabajo_final/camacho-lucia" target="_blank" style="color: #cd7f32; text-decoration: none; font-size: 0.75em; padding: 5px 14px; border: 1px solid #cd7f3250; border-radius: 20px; background: #cd7f3210;">Ver Entrega</a></div></div>
</div>


---

<h2 style="border: none;">Clasificados</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 10px; margin: 20px auto; max-width: 820px;">
<div class="challenger-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);"><div style="font-size: 1.3em; font-weight: 900; color: #555; min-width: 32px; text-align: center;">#4<div style="font-size: 0.42em; color: #888; font-weight: 600;">4sem</div></div><img src="https://github.com/fernandoramostrevi-ctrl.png" alt="@fernandoramostrevi-ctrl" style="width: 48px; height: 48px; border-radius: 50%; border: 2px solid #333; object-fit: cover; background: #2a2a3a; flex-shrink: 0;" onerror="this.style.display='none'"><div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;"><span style="font-weight: 700; color: #eee; font-size: 0.88em;">@fernandoramostrevi-ctrl</span><span style="background: rgba(231,76,60,0.15); border: 1px solid rgba(231,76,60,0.35); border-radius: 8px; padding: 1px 8px; font-size: 0.7em; color: #e74c3c;">&#9203; -25%</span></div><div style="width: 100%; margin: 6px 0 4px;"><div style="display: flex; align-items: center; gap: 4px; margin: 2px 0;"><span style="width: 14px; height: 14px; border-radius: 3px; flex-shrink: 0; background: #e8b84b; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.5em; color: #1a1a2e;">D</span><div style="flex: 1; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 95%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 3px;"></div></div><span style="font-size: 0.65em; color: #999; width: 24px; text-align: right;">9.5</span></div><div style="display: flex; align-items: center; gap: 4px; margin: 2px 0;"><span style="width: 14px; height: 14px; border-radius: 3px; flex-shrink: 0; background: #667eea; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.5em; color: #fff;">C</span><div style="flex: 1; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 100%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 3px;"></div></div><span style="font-size: 0.65em; color: #999; width: 24px; text-align: right;">10.0</span></div></div></div><div style="text-align: center; flex-shrink: 0;"><div style="font-size: 1.5em; font-weight: 900; color: #3498db; text-shadow: 0 0 8px rgba(52,152,219,0.3);">5.1</div><div style="display: flex; flex-direction: column; gap: 3px; align-items: center;"><a href="https://github.com/fernandoramostrevi-ctrl/ejercicios-bigdata/tree/main/entregas/trabajo_final/ramos_fernando" target="_blank" style="color: #667eea; text-decoration: none; font-size: 0.68em; border: 1px solid #667eea40; border-radius: 12px; padding: 2px 10px; display: inline-block;">Ver Entrega</a><a href="https://raw.githack.com/fernandoramostrevi-ctrl/ejercicios-bigdata/main/entregas/trabajo_final/ramos_fernando/outputs/dashboard/dashboard_asia_central.html" target="_blank" style="color: #2ecc71; text-decoration: none; font-size: 0.68em; border: 1px solid rgba(46,204,113,0.4); border-radius: 12px; padding: 2px 10px; display: inline-block;">Dashboard</a></div></div></div><div class="challenger-card" style="background: linear-gradient(180deg, #1a1a2e, #16213e); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);"><div style="font-size: 1.3em; font-weight: 900; color: #555; min-width: 32px; text-align: center;">#5<div style="font-size: 0.42em; color: #888; font-weight: 600;">4sem</div></div><img src="https://github.com/alxz0212.png" alt="@alxz0212" style="width: 48px; height: 48px; border-radius: 50%; border: 2px solid #333; object-fit: cover; background: #2a2a3a; flex-shrink: 0;" onerror="this.style.display='none'"><div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;"><span style="font-weight: 700; color: #eee; font-size: 0.88em;">@alxz0212</span><span style="background: rgba(231,76,60,0.15); border: 1px solid rgba(231,76,60,0.35); border-radius: 8px; padding: 1px 8px; font-size: 0.7em; color: #e74c3c;">&#9203; -25%</span></div><div style="width: 100%; margin: 6px 0 4px;"><div style="display: flex; align-items: center; gap: 4px; margin: 2px 0;"><span style="width: 14px; height: 14px; border-radius: 3px; flex-shrink: 0; background: #e8b84b; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.5em; color: #1a1a2e;">D</span><div style="flex: 1; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 0%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 3px;"></div></div><span style="font-size: 0.65em; color: #999; width: 24px; text-align: right;">0.0</span></div><div style="display: flex; align-items: center; gap: 4px; margin: 2px 0;"><span style="width: 14px; height: 14px; border-radius: 3px; flex-shrink: 0; background: #667eea; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.5em; color: #fff;">C</span><div style="flex: 1; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 70%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 3px;"></div></div><span style="font-size: 0.65em; color: #999; width: 24px; text-align: right;">7.0</span></div></div></div><div style="text-align: center; flex-shrink: 0;"><div style="font-size: 1.5em; font-weight: 900; color: #3498db; text-shadow: 0 0 8px rgba(52,152,219,0.3);">2.6</div><div style="display: flex; flex-direction: column; gap: 3px; align-items: center;"><a href="https://github.com/alxz0212/ejercicios-bigdata/tree/main/entregas/trabajo_final/Alexis_Mendoza" target="_blank" style="color: #667eea; text-decoration: none; font-size: 0.68em; border: 1px solid #667eea40; border-radius: 12px; padding: 2px 10px; display: inline-block;">Ver Entrega</a></div></div></div>
</div>


---

<h2 style="border: none;">Ranking Completo</h2>


| Pos | Estudiante | Nota | Estado | Proyecto | Fork |
|:---:|:-----------|:----:|:------:|:---------|:----:|
| **#1** (4sem) | @katitto | **8.7** &#10003; | &#9733; Destacado | `almache_katherine` | [Ver](https://github.com/katitto/ejercicios-bigdata/tree/main/entregas/trabajo_final/almache_katherine){target="_blank"} [Dashboard](https://raw.githack.com/katitto/ejercicios-bigdata/main/entregas/trabajo_final/almache_katherine/outputs/dashboard/index.html){target="_blank"} |
| **#2** (4sem) | @aurorafezu | **8.2** &#10003; | &#9733; Destacado | `fernandez_aurora` | [Ver](https://github.com/aurorafezu/ejercicios-bigdata/tree/main/entregas/trabajo_final/fernandez_aurora){target="_blank"} [Dashboard](https://raw.githack.com/aurorafezu/ejercicios-bigdata/main/entregas/trabajo_final/fernandez_aurora/dashboard_interactivo.html){target="_blank"} |
| **#3** (4sem) | @luuuuru | **7.0** &#10003; | &#10003; Aprobado | `camacho-lucia` | [Ver](https://github.com/luuuuru/ejercicios-bigdata/tree/main/entregas/trabajo_final/camacho-lucia){target="_blank"} |
| **#4** (4sem) | @fernandoramostrevi-ctrl | **5.1** &#9203;-25% | &#10003; Aprobado | `ramos_fernando` | [Ver](https://github.com/fernandoramostrevi-ctrl/ejercicios-bigdata/tree/main/entregas/trabajo_final/ramos_fernando){target="_blank"} [Dashboard](https://raw.githack.com/fernandoramostrevi-ctrl/ejercicios-bigdata/main/entregas/trabajo_final/ramos_fernando/outputs/dashboard/dashboard_asia_central.html){target="_blank"} |
| **#5** (4sem) | @alxz0212 | **2.6** &#9203;-25% | &#10007; Insuficiente | `Alexis_Mendoza` | [Ver](https://github.com/alxz0212/ejercicios-bigdata/tree/main/entregas/trabajo_final/Alexis_Mendoza){target="_blank"} |


---

<h2 style="border: none;">Distribucion de Notas</h2>

<div style="margin: 20px 0;">
<div style="display: flex; align-items: center; margin: 8px 0;"><span style="width: 130px; font-weight: bold; color: #ccc;">9-10 Excelente</span><div style="flex: 1; background: #333; border-radius: 5px; height: 28px; overflow: hidden;"><div style="width: 0%; background: linear-gradient(90deg, #f9d423, #ff4e50); height: 100%; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; min-width: 0px;"></div></div></div><div style="display: flex; align-items: center; margin: 8px 0;"><span style="width: 130px; font-weight: bold; color: #ccc;">7-8 Notable</span><div style="flex: 1; background: #333; border-radius: 5px; height: 28px; overflow: hidden;"><div style="width: 60%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; min-width: 35px;">3</div></div></div><div style="display: flex; align-items: center; margin: 8px 0;"><span style="width: 130px; font-weight: bold; color: #ccc;">5-6 Aprobado</span><div style="flex: 1; background: #333; border-radius: 5px; height: 28px; overflow: hidden;"><div style="width: 20%; background: linear-gradient(90deg, #43e97b, #38f9d7); height: 100%; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; min-width: 35px;">1</div></div></div><div style="display: flex; align-items: center; margin: 8px 0;"><span style="width: 130px; font-weight: bold; color: #ccc;"><5 Insuficiente</span><div style="flex: 1; background: #333; border-radius: 5px; height: 28px; overflow: hidden;"><div style="width: 20%; background: linear-gradient(90deg, #fa709a, #fee140); height: 100%; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; min-width: 35px;">1</div></div></div></div>


---

<div style="background: linear-gradient(180deg, #1a1a2e, #0f0f23); border-radius: 14px; padding: 24px 28px; margin: 30px 0; border: 1px solid rgba(255,255,255,0.05);"><h3 style="color: #ccc; margin: 0 0 16px; border: none; font-size: 1.05em;">&#955; Guia de lectura</h3><div style="display: flex; align-items: flex-start; gap: 10px; margin: 10px 0;"><div style="flex-shrink: 0; width: 36px; height: 24px; display: flex; align-items: center; justify-content: center;"><div style="display: inline-flex; align-items: center; gap: 4px; background: #1a1a2e; border-radius: 6px; padding: 3px 8px;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #e8b84b; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #1a1a2e;">D</span><div style="width: 30px; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 70%; background: linear-gradient(90deg, #e8b84b, #f9d423); height: 100%; border-radius: 3px;"></div></div></div></div><div><span style="font-weight: 700; color: #e8b84b;">D (Doc)</span><span style="color: #999;"> &mdash; Nota de documentacion (PROMPTS.md): calidad, autenticidad y estructura de los prompts entregados.</span></div></div><div style="display: flex; align-items: flex-start; gap: 10px; margin: 10px 0;"><div style="flex-shrink: 0; width: 36px; height: 24px; display: flex; align-items: center; justify-content: center;"><div style="display: inline-flex; align-items: center; gap: 4px; background: #1a1a2e; border-radius: 6px; padding: 3px 8px;"><span style="width: 16px; height: 16px; border-radius: 4px; flex-shrink: 0; background: #667eea; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.55em; color: #fff;">C</span><div style="width: 30px; background: #2a2a3a; border-radius: 3px; height: 5px; overflow: hidden;"><div style="width: 80%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 3px;"></div></div></div></div><div><span style="font-weight: 700; color: #667eea;">C (Cod)</span><span style="color: #999;"> &mdash; Nota de codigo: archivos Python, notebooks, SQL, configs y estructura del proyecto.</span></div></div><div style="display: flex; align-items: flex-start; gap: 10px; margin: 10px 0;"><div style="flex-shrink: 0; width: 36px; height: 24px; display: flex; align-items: center; justify-content: center;"><span style="font-weight: 900; color: #3498db; font-size: 1.1em;">8.7</span></div><div><span style="font-weight: 700; color: #3498db;">Nota</span><span style="color: #999;"> &mdash; La nota final combina Doc (60%) y Cod (40%). Si falta PROMPTS.md se aplica -30% adicional.</span></div></div><div style="margin: 14px 0 0; border-top: 1px solid #333; padding-top: 14px;"></div><div style="margin: 12px 0;"><div style="margin-bottom: 6px;"><span style="background: rgba(46,204,113,0.15); border: 1px solid rgba(46,204,113,0.35); border-radius: 8px; padding: 1px 8px; font-size: 0.75em; color: #2ecc71;">&#10003; Puntual</span></div><div style="color: #999; font-size: 0.92em; padding-left: 4px;">Entrega puntual: el trabajo fue entregado antes de la publicacion del ranking. La nota no tiene penalizacion.</div></div><div style="margin: 12px 0;"><div style="margin-bottom: 6px;"><span style="background: rgba(231,76,60,0.15); border: 1px solid rgba(231,76,60,0.35); border-radius: 8px; padding: 1px 8px; font-size: 0.75em; color: #e74c3c;">&#9203; -X%</span></div><div style="color: #999; font-size: 0.92em; padding-left: 4px;">Entrega tardia: el trabajo fue entregado despues de la publicacion del ranking. Se aplica una penalizacion proporcional al retraso:</div><div style="margin: 8px 0 0 4px; padding: 8px 14px; background: rgba(231,76,60,0.06); border-radius: 8px; border-left: 3px solid #e74c3c40;"><code style="color: #e74c3c; font-size: 0.85em;">0-24h: -15% | 1-3 dias: -25% | 3-7 dias: -40% | >7 dias: -50%</code></div></div></div>


---

<div style="background: linear-gradient(180deg, #1a1a2e, #0f0f23); border-radius: 14px; padding: 24px 28px; margin: 30px 0; border: 1px solid rgba(255,255,255,0.05);"><h3 style="color: #ccc; margin: 0 0 18px; border: none; font-size: 1.05em;">&#9881; Reglas del Ranking</h3><div style="margin: 14px 0; padding: 14px; background: rgba(249,212,35,0.04); border-radius: 10px; border-left: 3px solid #f9d42340;"><h4 style="color: #f9d423; margin: 0 0 8px; border: none; font-size: 0.95em;">&#916; Promocion 2026 (18 alumnos)</h4><p style="color: #999; font-size: 0.88em; margin: 0; line-height: 1.6;">Ventana de entrega: 13 feb - 31 mar 2026. Entregas puntuales (antes del 13 feb) mantienen su nota intacta. Entregas tardias reciben penalizacion progresiva: 0-24h (-15%), 1-3 dias (-25%), 3-7 dias (-40%), mas de 7 dias (-50%). Despues del 31 de marzo las notas se congelan definitivamente.</p></div><div style="margin: 14px 0; padding: 14px; background: rgba(102,126,234,0.04); border-radius: 10px; border-left: 3px solid #667eea40;"><h4 style="color: #667eea; margin: 0 0 8px; border: none; font-size: 0.95em;">&#8734; Comunidad (ranking anual)</h4><p style="color: #999; font-size: 0.88em; margin: 0; line-height: 1.6;">Cualquier persona puede completar el curso y aparecer en el ranking de su ano (2026, 2027...). Requisitos: fork con minimo 30 dias de antiguedad y entregas reales. No compiten con la Promocion 2026. Mismos criterios de evaluacion.</p></div><div style="margin: 14px 0 0; padding: 14px; background: rgba(46,204,113,0.04); border-radius: 10px; border-left: 3px solid #2ecc7140;"><h4 style="color: #2ecc71; margin: 0 0 8px; border: none; font-size: 0.95em;">&#931; Criterios de Evaluacion</h4><p style="color: #999; font-size: 0.88em; margin: 0; line-height: 1.6;">D (Doc, 60%): calidad, autenticidad y estructura del PROMPTS.md. C (Cod, 40%): archivos Python, notebooks, SQL y estructura del proyecto. Sin PROMPTS.md se aplica penalizacion adicional del 30%. La nota final puede verse afectada por similitud con el ejemplo del profesor.</p></div></div>


---

<h2 style="border: none;">Ranking Comunidad</h2>

<div style="text-align: center; padding: 30px 20px; background: linear-gradient(180deg, #1a1a2e, #0f0f23); border-radius: 14px; margin: 20px 0; border: 1px solid rgba(255,255,255,0.05);"><div style="font-size: 2em; margin-bottom: 10px;">&#8734;</div><p style="color: #888; font-size: 0.95em;">Aun no hay participantes de la comunidad. Haz un fork del repositorio, completa el curso y aparece aqui!</p></div>


---

<p style="text-align: center; color: #555; font-size: 0.85em; margin-top: 40px;">
El ranking se actualiza automaticamente con cada evaluacion. Entrega tu trabajo para aparecer!<br>
<em>Generado por: evaluar v3.0 | 2026-02-14 02:30</em>
</p>

---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias academicas:**
- Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
- McKinney, W. (2022). *Python for Data Analysis*, 3rd Ed. O'Reilly Media.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media.
