(() => {
  const overlay = document.getElementById("entry-overlay");
  const enterButton = document.getElementById("enter-site");
  const storageKey = "wind989-entry-seen-in-session";
  const replay = new URLSearchParams(window.location.search).has("welcome");

  if (!overlay || !enterButton) return;

  let hasVisited = false;
  try {
    hasVisited = window.sessionStorage.getItem(storageKey) === "true";
  } catch (_) {
    // 浏览器禁用会话存储时，欢迎动画会在每次刷新时播放。
  }

  if (hasVisited && !replay) return;

  document.body.classList.add("entry-active");
  overlay.setAttribute("aria-hidden", "false");

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      overlay.classList.add("entry-overlay--visible");
      enterButton.focus();
    });
  });

  const enterSite = () => {
    if (overlay.classList.contains("entry-overlay--leaving")) return;

    try {
      window.sessionStorage.setItem(storageKey, "true");
    } catch (_) {
      // 会话存储不可用时，不影响进入网站。
    }

    overlay.classList.add("entry-overlay--leaving");
    window.setTimeout(() => {
      document.body.classList.remove("entry-active");
      overlay.setAttribute("aria-hidden", "true");
      if (replay) {
        window.history.replaceState({}, "", `${window.location.pathname}${window.location.hash}`);
      }
    }, 700);
  };

  enterButton.addEventListener("click", enterSite);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") enterSite();
  });
})();
