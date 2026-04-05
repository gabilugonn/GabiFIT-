<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>GABFIT — Academia</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Barlow+Condensed:wght@300;400;600;700;900&family=Barlow:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
    :root {
      --black: #0a0a0a;
      --dark: #111111;
      --card: #161616;
      --border: #222222;
      --red: #e8001d;
      --red-dark: #b0001a;
      --red-glow: rgba(232,0,29,0.25);
      --white: #f5f5f5;
      --muted: #888888;
      --input-bg: #1a1a1a;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      background: var(--black);
      color: var(--white);
      font-family: 'Barlow', sans-serif;
      overflow-x: hidden;
    }

    /* ── NOISE OVERLAY ── */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 9999;
      opacity: 0.4;
    }

    /* ── NAV ── */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 18px 48px;
      background: rgba(10,10,10,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }

    .nav-logo {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 28px;
      letter-spacing: 4px;
      color: var(--white);
    }
    .nav-logo span { color: var(--red); }

    .nav-links {
      display: flex;
      gap: 36px;
      list-style: none;
    }
    .nav-links a {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      text-decoration: none;
      transition: color .2s;
    }
    .nav-links a:hover { color: var(--red); }

    .nav-cta {
      background: var(--red);
      color: var(--white) !important;
      padding: 10px 24px;
      border-radius: 2px;
      font-family: 'Barlow Condensed', sans-serif !important;
      font-weight: 700 !important;
      font-size: 12px !important;
      letter-spacing: 2px;
      text-transform: uppercase;
      transition: background .2s, box-shadow .2s !important;
    }
    .nav-cta:hover { background: var(--red-dark) !important; box-shadow: 0 0 24px var(--red-glow) !important; }

    /* ── HERO ── */
    #hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      position: relative;
      overflow: hidden;
      padding: 0 48px;
    }

    .hero-bg {
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 60% 60% at 70% 50%, rgba(232,0,29,0.12) 0%, transparent 70%),
        linear-gradient(135deg, #0a0a0a 0%, #111 100%);
    }

    .hero-lines {
      position: absolute;
      inset: 0;
      background-image:
        repeating-linear-gradient(90deg, transparent, transparent 79px, rgba(255,255,255,0.02) 79px, rgba(255,255,255,0.02) 80px);
    }

    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 780px;
    }

    .hero-tag {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .hero-tag::before {
      content: '';
      display: block;
      width: 40px;
      height: 2px;
      background: var(--red);
    }

    .hero-title {
      font-family: 'Black Han Sans', sans-serif;
      font-size: clamp(72px, 10vw, 140px);
      line-height: 0.92;
      letter-spacing: -2px;
      margin-bottom: 32px;
    }
    .hero-title .line-red { color: var(--red); }
    .hero-title .line-outline {
      -webkit-text-stroke: 2px var(--white);
      color: transparent;
    }

    .hero-subtitle {
      font-size: 17px;
      font-weight: 300;
      color: var(--muted);
      line-height: 1.7;
      max-width: 480px;
      margin-bottom: 48px;
    }

    .hero-btns {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }

    .btn-primary {
      background: var(--red);
      color: var(--white);
      padding: 16px 40px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      border: none;
      cursor: pointer;
      border-radius: 2px;
      text-decoration: none;
      display: inline-block;
      transition: all .25s;
      box-shadow: 0 0 0 var(--red-glow);
    }
    .btn-primary:hover {
      background: var(--red-dark);
      box-shadow: 0 8px 32px var(--red-glow);
      transform: translateY(-2px);
    }

    .btn-outline {
      background: transparent;
      color: var(--white);
      padding: 16px 40px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      border: 1px solid var(--border);
      cursor: pointer;
      border-radius: 2px;
      text-decoration: none;
      display: inline-block;
      transition: all .25s;
    }
    .btn-outline:hover {
      border-color: var(--red);
      color: var(--red);
      transform: translateY(-2px);
    }

    .hero-stats {
      position: absolute;
      right: 48px;
      bottom: 60px;
      display: flex;
      gap: 48px;
      z-index: 2;
    }
    .hero-stat-num {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 42px;
      color: var(--white);
      line-height: 1;
    }
    .hero-stat-num span { color: var(--red); }
    .hero-stat-label {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 6px;
    }

    /* ── SECTION COMMON ── */
    section { padding: 100px 48px; }

    .section-tag {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-tag::before {
      content: '';
      display: block;
      width: 28px;
      height: 2px;
      background: var(--red);
    }

    .section-title {
      font-family: 'Black Han Sans', sans-serif;
      font-size: clamp(36px, 5vw, 64px);
      line-height: 1;
      margin-bottom: 16px;
    }
    .section-title span { color: var(--red); }

    .section-sub {
      font-size: 16px;
      font-weight: 300;
      color: var(--muted);
      max-width: 520px;
      line-height: 1.7;
      margin-bottom: 60px;
    }

    /* ── PLANOS ── */
    #planos { background: var(--dark); }

    .plans-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2px;
    }

    .plan-card {
      background: var(--card);
      padding: 48px 36px;
      border: 1px solid var(--border);
      position: relative;
      cursor: pointer;
      transition: all .3s;
      overflow: hidden;
    }
    .plan-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: var(--border);
      transition: background .3s;
    }
    .plan-card:hover::before,
    .plan-card.featured::before { background: var(--red); }
    .plan-card:hover { border-color: rgba(232,0,29,0.3); transform: translateY(-4px); }

    .plan-card.featured {
      background: #1a0508;
      border-color: rgba(232,0,29,0.4);
    }

    .plan-badge {
      display: inline-block;
      background: var(--red);
      color: var(--white);
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 4px 12px;
      border-radius: 1px;
      margin-bottom: 24px;
    }

    .plan-name {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 32px;
      letter-spacing: 2px;
      margin-bottom: 8px;
    }

    .plan-desc {
      font-size: 13px;
      color: var(--muted);
      margin-bottom: 32px;
      line-height: 1.6;
    }

    .plan-price {
      margin-bottom: 36px;
    }
    .plan-price .currency {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 22px;
      font-weight: 600;
      color: var(--red);
      vertical-align: top;
      margin-top: 8px;
      display: inline-block;
    }
    .plan-price .amount {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 72px;
      line-height: 1;
      color: var(--white);
    }
    .plan-price .period {
      font-size: 13px;
      color: var(--muted);
      display: block;
      margin-top: 4px;
    }

    .plan-features {
      list-style: none;
      margin-bottom: 40px;
    }
    .plan-features li {
      font-size: 14px;
      color: #ccc;
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .plan-features li::before {
      content: '✓';
      color: var(--red);
      font-weight: 700;
      font-size: 12px;
    }
    .plan-features li.disabled {
      color: var(--muted);
      text-decoration: line-through;
      opacity: 0.5;
    }
    .plan-features li.disabled::before { content: '✕'; color: #555; }

    .plan-btn {
      width: 100%;
      padding: 14px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--white);
      cursor: pointer;
      border-radius: 2px;
      transition: all .25s;
    }
    .plan-btn:hover,
    .plan-card.featured .plan-btn {
      background: var(--red);
      border-color: var(--red);
      box-shadow: 0 8px 24px var(--red-glow);
    }

    /* ── INSCRIÇÃO ── */
    #inscricao { background: var(--black); }

    .form-container {
      background: var(--card);
      border: 1px solid var(--border);
      padding: 60px;
      max-width: 860px;
      position: relative;
    }
    .form-container::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: var(--red);
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }
    .form-grid.full { grid-template-columns: 1fr; }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .form-label {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
    }

    .form-input, .form-select {
      background: var(--input-bg);
      border: 1px solid var(--border);
      color: var(--white);
      padding: 14px 18px;
      font-family: 'Barlow', sans-serif;
      font-size: 15px;
      border-radius: 2px;
      outline: none;
      transition: border-color .2s, box-shadow .2s;
      appearance: none;
    }
    .form-input:focus, .form-select:focus {
      border-color: var(--red);
      box-shadow: 0 0 0 3px rgba(232,0,29,0.1);
    }
    .form-select option { background: var(--dark); }

    .form-section-title {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 22px;
      letter-spacing: 1px;
      margin: 36px 0 20px;
      color: var(--white);
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .form-section-title::before {
      content: '';
      display: block;
      width: 4px;
      height: 24px;
      background: var(--red);
      border-radius: 1px;
    }

    .plan-selector {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 24px;
    }

    .plan-option {
      border: 1px solid var(--border);
      padding: 16px;
      cursor: pointer;
      border-radius: 2px;
      transition: all .2s;
      position: relative;
    }
    .plan-option input[type="radio"] {
      position: absolute;
      opacity: 0;
      width: 0;
    }
    .plan-option:hover { border-color: var(--red); }
    .plan-option.selected {
      border-color: var(--red);
      background: rgba(232,0,29,0.08);
    }
    .plan-option-name {
      font-family: 'Barlow Condensed', sans-serif;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 1px;
      color: var(--white);
    }
    .plan-option-price {
      font-size: 12px;
      color: var(--red);
      margin-top: 4px;
    }

    .goal-selector {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 24px;
    }

    .goal-btn {
      padding: 10px 20px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--muted);
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      border-radius: 2px;
      transition: all .2s;
    }
    .goal-btn:hover, .goal-btn.active {
      border-color: var(--red);
      color: var(--white);
      background: rgba(232,0,29,0.1);
    }

    .form-submit {
      width: 100%;
      padding: 18px;
      background: var(--red);
      color: var(--white);
      border: none;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      cursor: pointer;
      border-radius: 2px;
      margin-top: 36px;
      transition: all .25s;
    }
    .form-submit:hover {
      background: var(--red-dark);
      box-shadow: 0 12px 40px var(--red-glow);
      transform: translateY(-2px);
    }

    /* ── TREINO ── */
    #treino { background: var(--dark); }

    .workout-builder {
      background: var(--card);
      border: 1px solid var(--border);
      padding: 48px;
      position: relative;
    }
    .workout-builder::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: var(--red);
    }

    .muscle-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 36px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
    }

    .muscle-tab {
      padding: 10px 22px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      background: transparent;
      border: 1px solid var(--border);
      color: var(--muted);
      cursor: pointer;
      border-radius: 2px;
      transition: all .2s;
    }
    .muscle-tab:hover { color: var(--white); border-color: #444; }
    .muscle-tab.active {
      background: var(--red);
      border-color: var(--red);
      color: var(--white);
    }

    .exercises-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 12px;
      margin-bottom: 36px;
    }

    .exercise-card {
      border: 1px solid var(--border);
      padding: 18px;
      cursor: pointer;
      border-radius: 2px;
      transition: all .2s;
      position: relative;
      background: var(--input-bg);
    }
    .exercise-card:hover { border-color: rgba(232,0,29,0.5); background: rgba(232,0,29,0.04); }
    .exercise-card.selected {
      border-color: var(--red);
      background: rgba(232,0,29,0.1);
    }
    .exercise-card.selected::after {
      content: '✓';
      position: absolute;
      top: 10px; right: 12px;
      color: var(--red);
      font-weight: 700;
      font-size: 14px;
    }

    .ex-icon {
      font-size: 24px;
      margin-bottom: 10px;
    }
    .ex-name {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.5px;
    }
    .ex-muscle {
      font-size: 11px;
      color: var(--muted);
      margin-top: 4px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .workout-list {
      background: var(--black);
      border: 1px solid var(--border);
      padding: 28px 32px;
      border-radius: 2px;
      min-height: 120px;
      margin-bottom: 24px;
    }

    .workout-list h3 {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 20px;
    }

    .workout-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
    }
    .workout-item:last-child { border-bottom: none; }

    .workout-item-info {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .workout-item-num {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 20px;
      color: var(--red);
      width: 28px;
    }
    .workout-item-name {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 16px;
      font-weight: 600;
      letter-spacing: 0.5px;
    }
    .workout-item-tag {
      font-size: 11px;
      color: var(--muted);
      text-transform: uppercase;
    }

    .workout-item-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sets-input {
      background: var(--input-bg);
      border: 1px solid var(--border);
      color: var(--white);
      padding: 6px 12px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 14px;
      font-weight: 600;
      border-radius: 2px;
      width: 72px;
      text-align: center;
      outline: none;
    }
    .sets-input:focus { border-color: var(--red); }

    .remove-btn {
      background: transparent;
      border: 1px solid #333;
      color: var(--muted);
      width: 30px;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border-radius: 2px;
      font-size: 16px;
      transition: all .2s;
    }
    .remove-btn:hover { border-color: var(--red); color: var(--red); }

    .empty-workout {
      text-align: center;
      color: var(--muted);
      font-size: 14px;
      padding: 20px 0;
    }

    .workout-actions {
      display: flex;
      gap: 12px;
    }

    .btn-save-workout {
      flex: 1;
      padding: 16px;
      background: var(--red);
      color: var(--white);
      border: none;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      cursor: pointer;
      border-radius: 2px;
      transition: all .25s;
    }
    .btn-save-workout:hover {
      background: var(--red-dark);
      box-shadow: 0 8px 24px var(--red-glow);
    }

    .btn-clear-workout {
      padding: 16px 28px;
      background: transparent;
      color: var(--muted);
      border: 1px solid var(--border);
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      cursor: pointer;
      border-radius: 2px;
      transition: all .2s;
    }
    .btn-clear-workout:hover { border-color: #555; color: var(--white); }

    .workout-name-input {
      width: 100%;
      background: var(--input-bg);
      border: 1px solid var(--border);
      color: var(--white);
      padding: 14px 18px;
      font-family: 'Barlow', sans-serif;
      font-size: 15px;
      border-radius: 2px;
      outline: none;
      margin-bottom: 24px;
      transition: border-color .2s;
    }
    .workout-name-input:focus { border-color: var(--red); }
    .workout-name-input::placeholder { color: #444; }

    /* ── SAVED WORKOUTS ── */
    .saved-workouts {
      margin-top: 48px;
    }
    .saved-workout-card {
      background: var(--black);
      border: 1px solid var(--border);
      padding: 24px 28px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      transition: border-color .2s;
    }
    .saved-workout-card:hover { border-color: rgba(232,0,29,0.3); }
    .saved-workout-name {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 18px;
      letter-spacing: 1px;
    }
    .saved-workout-meta {
      font-size: 12px;
      color: var(--muted);
      margin-top: 4px;
    }
    .saved-workout-exercises {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 10px;
    }
    .exercise-pill {
      background: var(--card);
      border: 1px solid var(--border);
      padding: 4px 10px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--muted);
      border-radius: 2px;
    }
    .delete-workout-btn {
      background: transparent;
      border: 1px solid #2a2a2a;
      color: var(--muted);
      padding: 8px 14px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      border-radius: 2px;
      white-space: nowrap;
      transition: all .2s;
      flex-shrink: 0;
    }
    .delete-workout-btn:hover { border-color: var(--red); color: var(--red); }

    /* ── FOOTER ── */
    footer {
      background: var(--dark);
      border-top: 1px solid var(--border);
      padding: 60px 48px 40px;
    }

    .footer-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 48px;
      margin-bottom: 60px;
      flex-wrap: wrap;
    }

    .footer-logo {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 36px;
      letter-spacing: 4px;
    }
    .footer-logo span { color: var(--red); }
    .footer-tagline {
      font-size: 13px;
      color: var(--muted);
      margin-top: 8px;
      font-weight: 300;
    }

    .footer-links h4 {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 20px;
    }
    .footer-links ul { list-style: none; }
    .footer-links li {
      font-size: 14px;
      color: var(--muted);
      margin-bottom: 10px;
      cursor: pointer;
      transition: color .2s;
    }
    .footer-links li:hover { color: var(--white); }

    .footer-bottom {
      border-top: 1px solid var(--border);
      padding-top: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .footer-copy {
      font-size: 12px;
      color: #444;
    }

    /* ── TOAST ── */
    .toast {
      position: fixed;
      bottom: 32px;
      right: 32px;
      background: var(--card);
      border: 1px solid var(--red);
      border-left: 4px solid var(--red);
      color: var(--white);
      padding: 18px 28px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 15px;
      font-weight: 600;
      letter-spacing: 1px;
      border-radius: 2px;
      z-index: 9999;
      transform: translateY(80px);
      opacity: 0;
      transition: all .35s cubic-bezier(.16,1,.3,1);
      box-shadow: 0 12px 40px rgba(0,0,0,0.4);
    }
    .toast.show { transform: translateY(0); opacity: 1; }

    /* ── SCROLL ANIMATION ── */
    .fade-in {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity .6s ease, transform .6s ease;
    }
    .fade-in.visible { opacity: 1; transform: translateY(0); }

    /* ── MOBILE ── */
    @media (max-width: 768px) {
      nav { padding: 16px 20px; }
      .nav-links { display: none; }
      #hero { padding: 0 20px; }
      section { padding: 60px 20px; }
      .hero-stats { right: 20px; bottom: 40px; gap: 24px; }
      .hero-stat-num { font-size: 28px; }
      .form-container { padding: 32px 20px; }
      .form-grid { grid-template-columns: 1fr; }
      .plan-selector { grid-template-columns: 1fr; }
      .workout-builder { padding: 28px 20px; }
      .workout-actions { flex-direction: column; }
      footer { padding: 40px 20px; }
      .footer-top { flex-direction: column; gap: 32px; }
      .footer-bottom { flex-direction: column; text-align: center; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">GAB<span>FIT</span></div>
  <ul class="nav-links">
    <li><a href="#planos">Planos</a></li>
    <li><a href="#inscricao">Inscrição</a></li>
    <li><a href="#treino">Montar Treino</a></li>
    <li><a href="#inscricao" class="nav-cta">Começar Agora</a></li>
  </ul>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-lines"></div>

  <div class="hero-content">
    <div class="hero-tag">Academia Gabfit — Resultados Reais</div>
    <h1 class="hero-title">
      SUPERE<br>
      <span class="line-red">SEUS</span><br>
      <span class="line-outline">LIMITES</span>
    </h1>
    <p class="hero-subtitle">
      Transforme seu corpo e sua mentalidade. Na Gabfit, cada treino é uma conquista, cada gota de suor é um passo rumo à sua melhor versão.
    </p>
    <div class="hero-btns">
      <a href="#inscricao" class="btn-primary">Inscreva-se Agora</a>
      <a href="#planos" class="btn-outline">Ver Planos</a>
    </div>
  </div>

  <div class="hero-stats">
    <div>
      <div class="hero-stat-num">500<span>+</span></div>
      <div class="hero-stat-label">Alunos Ativos</div>
    </div>
    <div>
      <div class="hero-stat-num">15<span>+</span></div>
      <div class="hero-stat-label">Equipamentos</div>
    </div>
    <div>
      <div class="hero-stat-num">6<span>h</span></div>
      <div class="hero-stat-label">Atendimento</div>
    </div>
  </div>
</section>

<!-- PLANOS -->
<section id="planos">
  <div class="section-tag">Nossos Planos</div>
  <h2 class="section-title">ESCOLHA SEU <span>PLANO</span></h2>
  <p class="section-sub">Planos flexíveis para todos os objetivos e bolsos. Comece hoje mesmo.</p>

  <div class="plans-grid fade-in">
    <!-- Básico -->
    <div class="plan-card">
      <div class="plan-name">BÁSICO</div>
      <p class="plan-desc">Ideal para quem está começando e quer experimentar a Gabfit.</p>
      <div class="plan-price">
        <span class="currency">R$</span>
        <span class="amount">89</span>
        <span class="period">por mês</span>
      </div>
      <ul class="plan-features">
        <li>Acesso à musculação</li>
        <li>Uso de vestiário</li>
        <li>1 avaliação física/mês</li>
        <li class="disabled">Aulas coletivas</li>
        <li class="disabled">Personal trainer incluso</li>
        <li class="disabled">Nutricionista</li>
      </ul>
      <button class="plan-btn" onclick="selectPlan('Básico — R$89/mês')">Escolher Plano</button>
    </div>

    <!-- Intermediário (destaque) -->
    <div class="plan-card featured">
      <div class="plan-badge">Mais Popular</div>
      <div class="plan-name">PRO</div>
      <p class="plan-desc">Perfeito para quem quer resultados mais rápidos com suporte completo.</p>
      <div class="plan-price">
        <span class="currency">R$</span>
        <span class="amount">149</span>
        <span class="period">por mês</span>
      </div>
      <ul class="plan-features">
        <li>Acesso à musculação</li>
        <li>Uso de vestiário</li>
        <li>2 avaliações físicas/mês</li>
        <li>Aulas coletivas ilimitadas</li>
        <li>2h Personal trainer/semana</li>
        <li class="disabled">Nutricionista</li>
      </ul>
      <button class="plan-btn" onclick="selectPlan('Pro — R$149/mês')">Escolher Plano</button>
    </div>

    <!-- Premium -->
    <div class="plan-card">
      <div class="plan-name">ELITE</div>
      <p class="plan-desc">Experiência premium com tudo que a Gabfit tem a oferecer.</p>
      <div class="plan-price">
        <span class="currency">R$</span>
        <span class="amount">229</span>
        <span class="period">por mês</span>
      </div>
      <ul class="plan-features">
        <li>Acesso à musculação</li>
        <li>Uso de vestiário premium</li>
        <li>Avaliações físicas ilimitadas</li>
        <li>Aulas coletivas ilimitadas</li>
        <li>Personal trainer ilimitado</li>
        <li>Consulta com nutricionista</li>
      </ul>
      <button class="plan-btn" onclick="selectPlan('Elite — R$229/mês')">Escolher Plano</button>
    </div>
  </div>
</section>

<!-- INSCRIÇÃO -->
<section id="inscricao">
  <div class="section-tag">Inscrição</div>
  <h2 class="section-title">FAÇA SUA <span>INSCRIÇÃO</span></h2>
  <p class="section-sub">Preencha seus dados e comece sua jornada na Gabfit hoje mesmo.</p>

  <div class="form-container fade-in">
    <div class="form-section-title">Dados Pessoais</div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Nome Completo *</label>
        <input class="form-input" type="text" id="nome" placeholder="Seu nome completo" />
      </div>
      <div class="form-group">
        <label class="form-label">Data de Nascimento *</label>
        <input class="form-input" type="date" id="nascimento" />
      </div>
    </div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">CPF *</label>
        <input class="form-input" type="text" id="cpf" placeholder="000.000.000-00" maxlength="14" />
      </div>
      <div class="form-group">
        <label class="form-label">RG</label>
        <input class="form-input" type="text" id="rg" placeholder="00.000.000-0" />
      </div>
    </div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">E-mail *</label>
        <input class="form-input" type="email" id="email" placeholder="seuemail@exemplo.com" />
      </div>
      <div class="form-group">
        <label class="form-label">Telefone / WhatsApp *</label>
        <input class="form-input" type="tel" id="telefone" placeholder="(00) 00000-0000" maxlength="15" />
      </div>
    </div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Gênero</label>
        <select class="form-select" id="genero">
          <option value="">Selecione</option>
          <option>Masculino</option>
          <option>Feminino</option>
          <option>Não-binário</option>
          <option>Prefiro não informar</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Como nos conheceu?</label>
        <select class="form-select" id="origem">
          <option value="">Selecione</option>
          <option>Instagram</option>
          <option>Indicação de amigo</option>
          <option>Google</option>
          <option>Panfleto</option>
          <option>Passou em frente</option>
        </select>
      </div>
    </div>

    <div class="form-section-title">Endereço</div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">CEP</label>
        <input class="form-input" type="text" id="cep" placeholder="00000-000" maxlength="9" />
      </div>
      <div class="form-group">
        <label class="form-label">Cidade / Estado</label>
        <input class="form-input" type="text" id="cidade" placeholder="Cidade — UF" />
      </div>
    </div>
    <div class="form-grid full">
      <div class="form-group">
        <label class="form-label">Endereço Completo</label>
        <input class="form-input" type="text" id="endereco" placeholder="Rua, número, bairro" />
      </div>
    </div>

    <div class="form-section-title">Dados Físicos</div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Peso (kg)</label>
        <input class="form-input" type="number" id="peso" placeholder="Ex: 75" />
      </div>
      <div class="form-group">
        <label class="form-label">Altura (cm)</label>
        <input class="form-input" type="number" id="altura" placeholder="Ex: 175" />
      </div>
    </div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Nível de Experiência</label>
        <select class="form-select" id="nivel">
          <option value="">Selecione</option>
          <option>Iniciante (nunca treinei)</option>
          <option>Básico (até 6 meses)</option>
          <option>Intermediário (6 meses–2 anos)</option>
          <option>Avançado (2+ anos)</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Frequência Desejada</label>
        <select class="form-select" id="frequencia">
          <option value="">Selecione</option>
          <option>2x por semana</option>
          <option>3x por semana</option>
          <option>4x por semana</option>
          <option>5x ou mais por semana</option>
        </select>
      </div>
    </div>

    <div class="form-section-title">Objetivo Principal</div>
    <div class="goal-selector" id="goalSelector">
      <button class="goal-btn" onclick="toggleGoal(this)">💪 Ganhar Massa</button>
      <button class="goal-btn" onclick="toggleGoal(this)">🔥 Perder Peso</button>
      <button class="goal-btn" onclick="toggleGoal(this)">❤️ Saúde & Bem-estar</button>
      <button class="goal-btn" onclick="toggleGoal(this)">⚡ Condicionamento</button>
      <button class="goal-btn" onclick="toggleGoal(this)">🏋️ Força & Potência</button>
      <button class="goal-btn" onclick="toggleGoal(this)">🧘 Flexibilidade</button>
      <button class="goal-btn" onclick="toggleGoal(this)">🏃 Resistência</button>
      <button class="goal-btn" onclick="toggleGoal(this)">🩺 Reabilitação</button>
    </div>

    <div class="form-section-title">Plano Escolhido</div>
    <div class="plan-selector" id="planSelector">
      <label class="plan-option" id="opt-basico" onclick="activatePlan('opt-basico')">
        <input type="radio" name="plano" value="basico" />
        <div class="plan-option-name">BÁSICO</div>
        <div class="plan-option-price">R$ 89/mês</div>
      </label>
      <label class="plan-option" id="opt-pro" onclick="activatePlan('opt-pro')">
        <input type="radio" name="plano" value="pro" />
        <div class="plan-option-name">PRO</div>
        <div class="plan-option-price">R$ 149/mês</div>
      </label>
      <label class="plan-option" id="opt-elite" onclick="activatePlan('opt-elite')">
        <input type="radio" name="plano" value="elite" />
        <div class="plan-option-name">ELITE</div>
        <div class="plan-option-price">R$ 229/mês</div>
      </label>
    </div>

    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Forma de Pagamento</label>
        <select class="form-select" id="pagamento">
          <option value="">Selecione</option>
          <option>Cartão de Crédito</option>
          <option>Cartão de Débito</option>
          <option>PIX</option>
          <option>Boleto</option>
          <option>Dinheiro</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Turno Preferido</label>
        <select class="form-select" id="turno">
          <option value="">Selecione</option>
          <option>Manhã (06h–12h)</option>
          <option>Tarde (12h–18h)</option>
          <option>Noite (18h–22h)</option>
        </select>
      </div>
    </div>

    <button class="form-submit" onclick="submitForm()">✦ CONFIRMAR INSCRIÇÃO</button>
  </div>
</section>

<!-- MONTAR TREINO -->
<section id="treino">
  <div class="section-tag">Treino Personalizado</div>
  <h2 class="section-title">MONTE SEU <span>TREINO</span></h2>
  <p class="section-sub">Selecione os exercícios por grupo muscular e monte sua ficha de treino personalizada.</p>

  <div class="workout-builder fade-in">
    <input class="workout-name-input" type="text" id="workoutName" placeholder="Nome do treino (ex: Treino A — Peito e Tríceps)" />

    <div class="muscle-tabs" id="muscleTabs">
      <button class="muscle-tab active" onclick="setMuscle(this, 'peito')">Peito</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'costas')">Costas</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'pernas')">Pernas</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'ombros')">Ombros</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'biceps')">Bíceps</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'triceps')">Tríceps</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'abdomen')">Abdômen</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'gluteos')">Glúteos</button>
      <button class="muscle-tab" onclick="setMuscle(this, 'cardio')">Cardio</button>
    </div>

    <div class="exercises-grid" id="exercisesGrid"></div>

    <div class="workout-list">
      <h3>✦ Treino Montado — <span id="workoutCount">0</span> exercício(s)</h3>
      <div id="workoutItems"></div>
    </div>

    <div class="workout-actions">
      <button class="btn-save-workout" onclick="saveWorkout()">💾 Salvar Treino</button>
      <button class="btn-clear-workout" onclick="clearWorkout()">Limpar</button>
    </div>

    <div class="saved-workouts" id="savedWorkoutsSection" style="display:none">
      <div class="form-section-title">Treinos Salvos</div>
      <div id="savedWorkoutsList"></div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-top">
    <div>
      <div class="footer-logo">GAB<span>FIT</span></div>
      <div class="footer-tagline">Supere seus limites. Todos os dias.</div>
    </div>
    <div class="footer-links">
      <h4>Academia</h4>
      <ul>
        <li>Sobre Nós</li>
        <li>Nossa Equipe</li>
        <li>Estrutura</li>
        <li>Galeria</li>
      </ul>
    </div>
    <div class="footer-links">
      <h4>Serviços</h4>
      <ul>
        <li>Musculação</li>
        <li>Aulas Coletivas</li>
        <li>Personal Trainer</li>
        <li>Nutrição</li>
      </ul>
    </div>
    <div class="footer-links">
      <h4>Contato</h4>
      <ul>
        <li>📍 Rua Exemplo, 123</li>
        <li>📞 (00) 90000-0000</li>
        <li>📧 contato@gabfit.com.br</li>
        <li>@gabfit.academia</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">© 2025 GABFIT Academia. Todos os direitos reservados.</div>
    <div class="footer-copy">Feito com 🔥 para os guerreiros</div>
  </div>
</footer>

<div class="toast" id="toast"></div>

<script>
  // ── EXERCISES DATA ──
  const exercises = {
    peito: [
      { name: 'Supino Reto', icon: '🏋️', muscle: 'Peito' },
      { name: 'Supino Inclinado', icon: '🏋️', muscle: 'Peito Superior' },
      { name: 'Supino Declinado', icon: '🏋️', muscle: 'Peito Inferior' },
      { name: 'Crucifixo Reto', icon: '🤸', muscle: 'Peito' },
      { name: 'Crucifixo Inclinado', icon: '🤸', muscle: 'Peito Superior' },
      { name: 'Peck Deck (Borboleta)', icon: '🦋', muscle: 'Peito' },
      { name: 'Crossover', icon: '🔀', muscle: 'Peito' },
      { name: 'Flexão de Braço', icon: '💪', muscle: 'Peito/Tríceps' },
      { name: 'Pullover', icon: '🔄', muscle: 'Peito/Dorsal' },
    ],
    costas: [
      { name: 'Puxada Alta (Pulley)', icon: '⬇️', muscle: 'Dorsal' },
      { name: 'Remada Curvada', icon: '🚣', muscle: 'Dorsal/Trapézio' },
      { name: 'Remada Unilateral', icon: '🚣', muscle: 'Dorsal' },
      { name: 'Remada Cavalinho', icon: '🚣', muscle: 'Costas Inteira' },
      { name: 'Levantamento Terra', icon: '🏋️', muscle: 'Lombar/Dorsal' },
      { name: 'Barra Fixa', icon: '🔝', muscle: 'Dorsal' },
      { name: 'Puxada Frente', icon: '⬆️', muscle: 'Dorsal' },
      { name: 'Hiperextensão', icon: '📐', muscle: 'Lombar' },
      { name: 'Serrote', icon: '🔨', muscle: 'Dorsal Médio' },
    ],
    pernas: [
      { name: 'Agachamento Livre', icon: '🏋️', muscle: 'Quadríceps/Glúteos' },
      { name: 'Leg Press 45°', icon: '🦵', muscle: 'Quadríceps' },
      { name: 'Cadeira Extensora', icon: '🦵', muscle: 'Quadríceps' },
      { name: 'Mesa Flexora', icon: '🔄', muscle: 'Isquiotibiais' },
      { name: 'Stiff', icon: '🧍', muscle: 'Posterior' },
      { name: 'Afundo', icon: '🚶', muscle: 'Quadríceps/Glúteos' },
      { name: 'Panturrilha em Pé', icon: '👟', muscle: 'Panturrilha' },
      { name: 'Hack Squat', icon: '🏋️', muscle: 'Quadríceps' },
      { name: 'Cadeira Adutora', icon: '🔀', muscle: 'Adutores' },
      { name: 'Abdutora', icon: '↔️', muscle: 'Abdutores' },
    ],
    ombros: [
      { name: 'Desenvolvimento com Halteres', icon: '🔼', muscle: 'Deltóide' },
      { name: 'Elevação Lateral', icon: '↔️', muscle: 'Deltóide Médio' },
      { name: 'Elevação Frontal', icon: '⬆️', muscle: 'Deltóide Anterior' },
      { name: 'Elevação Posterior', icon: '🔄', muscle: 'Deltóide Posterior' },
      { name: 'Desenvolvimento Militar', icon: '🏋️', muscle: 'Deltóide' },
      { name: 'Encolhimento (Trapézio)', icon: '⬆️', muscle: 'Trapézio' },
      { name: 'Crucifixo Invertido', icon: '🦅', muscle: 'Deltóide Posterior' },
      { name: 'Arnold Press', icon: '💪', muscle: 'Deltóide Completo' },
    ],
    biceps: [
      { name: 'Rosca Direta (Barra)', icon: '💪', muscle: 'Bíceps' },
      { name: 'Rosca Alternada', icon: '🔄', muscle: 'Bíceps' },
      { name: 'Rosca Concentrada', icon: '🎯', muscle: 'Bíceps' },
      { name: 'Rosca Scott', icon: '📐', muscle: 'Bíceps' },
      { name: 'Rosca Martelo', icon: '🔨', muscle: 'Braquial' },
      { name: 'Rosca 21', icon: '🔢', muscle: 'Bíceps Completo' },
      { name: 'Rosca Spider', icon: '🕷️', muscle: 'Bíceps' },
      { name: 'Rosca no Pulley', icon: '⬇️', muscle: 'Bíceps' },
    ],
    triceps: [
      { name: 'Tríceps Pulley (Corda)', icon: '🪢', muscle: 'Tríceps' },
      { name: 'Tríceps Francês', icon: '🏋️', muscle: 'Cabeça Longa' },
      { name: 'Tríceps Mergulho (Banco)', icon: '⬇️', muscle: 'Tríceps' },
      { name: 'Tríceps Coice', icon: '🦵', muscle: 'Tríceps' },
      { name: 'Extensão Testa', icon: '😤', muscle: 'Tríceps' },
      { name: 'Supino Fechado', icon: '🏋️', muscle: 'Tríceps/Peito' },
      { name: 'Tríceps Corda Acima', icon: '⬆️', muscle: 'Cabeça Longa' },
      { name: 'Paralelas', icon: '🔧', muscle: 'Tríceps' },
    ],
    abdomen: [
      { name: 'Abdominal Crunch', icon: '🧱', muscle: 'Reto Abdominal' },
      { name: 'Abdominal Infra', icon: '⬇️', muscle: 'Infra-abdominal' },
      { name: 'Prancha (Plank)', icon: '🟩', muscle: 'Core' },
      { name: 'Oblíquo com Cabo', icon: '🔄', muscle: 'Oblíquos' },
      { name: 'Elevação de Pernas', icon: '⬆️', muscle: 'Abdômen Inferior' },
      { name: 'Russian Twist', icon: '🔀', muscle: 'Oblíquos' },
      { name: 'Roda Abdominal', icon: '🛞', muscle: 'Core Completo' },
      { name: 'Bicicleta', icon: '🚴', muscle: 'Reto/Oblíquos' },
    ],
    gluteos: [
      { name: 'Hip Thrust', icon: '🍑', muscle: 'Glúteo Máximo' },
      { name: 'Glúteo na Polia', icon: '🔗', muscle: 'Glúteo' },
      { name: 'Passada (Avanço)', icon: '🚶', muscle: 'Glúteo/Quadríceps' },
      { name: 'Agachamento Sumo', icon: '🦵', muscle: 'Glúteo/Adutores' },
      { name: 'Elevação Quadrupede', icon: '🐾', muscle: 'Glúteo' },
      { name: 'Mesa Flexora (Glúteo)', icon: '🔄', muscle: 'Glúteo' },
      { name: 'Stiff Romeno', icon: '🧍', muscle: 'Posterior/Glúteo' },
      { name: 'Clamshell', icon: '🦪', muscle: 'Glúteo Médio' },
    ],
    cardio: [
      { name: 'Esteira', icon: '🏃', muscle: 'Cardio' },
      { name: 'Bicicleta Ergométrica', icon: '🚴', muscle: 'Cardio' },
      { name: 'Elíptico', icon: '🔄', muscle: 'Cardio Total' },
      { name: 'Corda de Pular', icon: '🪢', muscle: 'Cardio/HIIT' },
      { name: 'Remo Ergométrico', icon: '🚣', muscle: 'Cardio/Costas' },
      { name: 'Escada (Stairmaster)', icon: '🪜', muscle: 'Cardio/Glúteo' },
      { name: 'Burpee', icon: '💥', muscle: 'Cardio Total' },
      { name: 'Jumping Jack', icon: '⭐', muscle: 'Cardio' },
    ],
  };

  let currentMuscle = 'peito';
  let workoutList = [];
  let savedWorkouts = JSON.parse(localStorage.getItem('gabfit_workouts') || '[]');

  function setMuscle(el, muscle) {
    document.querySelectorAll('.muscle-tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
    currentMuscle = muscle;
    renderExercises();
  }

  function renderExercises() {
    const grid = document.getElementById('exercisesGrid');
    const list = exercises[currentMuscle] || [];
    grid.innerHTML = list.map((ex, i) => {
      const inWorkout = workoutList.find(w => w.name === ex.name);
      return `<div class="exercise-card ${inWorkout ? 'selected' : ''}" onclick="toggleExercise('${ex.name}', '${ex.muscle}', '${ex.icon}')">
        <div class="ex-icon">${ex.icon}</div>
        <div class="ex-name">${ex.name}</div>
        <div class="ex-muscle">${ex.muscle}</div>
      </div>`;
    }).join('');
  }

  function toggleExercise(name, muscle, icon) {
    const idx = workoutList.findIndex(w => w.name === name);
    if (idx >= 0) {
      workoutList.splice(idx, 1);
    } else {
      workoutList.push({ name, muscle, icon, series: '3', reps: '12' });
    }
    renderExercises();
    renderWorkoutList();
  }

  function renderWorkoutList() {
    const container = document.getElementById('workoutItems');
    const count = document.getElementById('workoutCount');
    count.textContent = workoutList.length;
    if (workoutList.length === 0) {
      container.innerHTML = '<div class="empty-workout">Nenhum exercício selecionado. Clique nos exercícios acima para adicionar ao treino.</div>';
      return;
    }
    container.innerHTML = workoutList.map((ex, i) => `
      <div class="workout-item">
        <div class="workout-item-info">
          <div class="workout-item-num">${String(i+1).padStart(2,'0')}</div>
          <div>
            <div class="workout-item-name">${ex.icon} ${ex.name}</div>
            <div class="workout-item-tag">${ex.muscle}</div>
          </div>
        </div>
        <div class="workout-item-controls">
          <input class="sets-input" type="text" value="${ex.series}x${ex.reps}" placeholder="3x12"
            onchange="updateSets(${i}, this.value)" title="Séries x Repetições" />
          <button class="remove-btn" onclick="removeExercise(${i})">×</button>
        </div>
      </div>
    `).join('');
  }

  function updateSets(idx, val) {
    workoutList[idx].setsReps = val;
  }

  function removeExercise(idx) {
    workoutList.splice(idx, 1);
    renderExercises();
    renderWorkoutList();
  }

  function clearWorkout() {
    workoutList = [];
    document.getElementById('workoutName').value = '';
    renderExercises();
    renderWorkoutList();
  }

  function saveWorkout() {
    if (workoutList.length === 0) { showToast('⚠️ Adicione exercícios ao treino!'); return; }
    const name = document.getElementById('workoutName').value.trim() || `Treino ${savedWorkouts.length + 1}`;
    const workout = {
      id: Date.now(),
      name,
      date: new Date().toLocaleDateString('pt-BR'),
      exercises: [...workoutList],
    };
    savedWorkouts.unshift(workout);
    localStorage.setItem('gabfit_workouts', JSON.stringify(savedWorkouts));
    showToast(`✅ Treino "${name}" salvo com sucesso!`);
    renderSavedWorkouts();
    clearWorkout();
  }

  function renderSavedWorkouts() {
    const section = document.getElementById('savedWorkoutsSection');
    const list = document.getElementById('savedWorkoutsList');
    if (savedWorkouts.length === 0) { section.style.display = 'none'; return; }
    section.style.display = 'block';
    list.innerHTML = savedWorkouts.map(w => `
      <div class="saved-workout-card">
        <div>
          <div class="saved-workout-name">${w.name}</div>
          <div class="saved-workout-meta">📅 ${w.date} — ${w.exercises.length} exercício(s)</div>
          <div class="saved-workout-exercises">
            ${w.exercises.map(e => `<span class="exercise-pill">${e.name}</span>`).join('')}
          </div>
        </div>
        <button class="delete-workout-btn" onclick="deleteWorkout(${w.id})">Excluir</button>
      </div>
    `).join('');
  }

  function deleteWorkout(id) {
    savedWorkouts = savedWorkouts.filter(w => w.id !== id);
    localStorage.setItem('gabfit_workouts', JSON.stringify(savedWorkouts));
    renderSavedWorkouts();
    showToast('🗑️ Treino removido.');
  }

  // ── FORM ──
  function selectPlan(planName) {
    document.getElementById('inscricao').scrollIntoView({ behavior: 'smooth' });
    const map = { 'Básico': 'opt-basico', 'Pro': 'opt-pro', 'Elite': 'opt-elite' };
    const key = Object.keys(map).find(k => planName.startsWith(k));
    if (key) activatePlan(map[key]);
  }

  function activatePlan(id) {
    document.querySelectorAll('.plan-option').forEach(o => o.classList.remove('selected'));
    document.getElementById(id)?.classList.add('selected');
  }

  function toggleGoal(btn) {
    btn.classList.toggle('active');
  }

  function submitForm() {
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const telefone = document.getElementById('telefone').value.trim();
    const selectedPlan = document.querySelector('.plan-option.selected');

    if (!nome) { showToast('⚠️ Informe seu nome completo!'); return; }
    if (!email) { showToast('⚠️ Informe seu e-mail!'); return; }
    if (!telefone) { showToast('⚠️ Informe seu telefone!'); return; }
    if (!selectedPlan) { showToast('⚠️ Selecione um plano!'); return; }

    showToast(`🎉 Inscrição realizada! Bem-vindo(a) à Gabfit, ${nome.split(' ')[0]}!`);
    setTimeout(() => showToast('📲 Em breve entraremos em contato pelo WhatsApp!'), 3000);
  }

  // ── TOAST ──
  function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3500);
  }

  // ── SCROLL ANIMATION ──
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  // ── CPF MASK ──
  document.getElementById('cpf').addEventListener('input', function () {
    let v = this.value.replace(/\D/g, '');
    v = v.replace(/(\d{3})(\d)/, '$1.$2');
    v = v.replace(/(\d{3})(\d)/, '$1.$2');
    v = v.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    this.value = v;
  });

  document.getElementById('telefone').addEventListener('input', function () {
    let v = this.value.replace(/\D/g, '');
    v = v.replace(/^(\d{2})(\d)/, '($1) $2');
    v = v.replace(/(\d{5})(\d)/, '$1-$2');
    this.value = v;
  });

  document.getElementById('cep').addEventListener('input', function () {
    let v = this.value.replace(/\D/g, '');
    v = v.replace(/(\d{5})(\d)/, '$1-$2');
    this.value = v;
  });

  // ── INIT ──
  renderExercises();
  renderWorkoutList();
  renderSavedWorkouts();
</script>
</body>
</html>
