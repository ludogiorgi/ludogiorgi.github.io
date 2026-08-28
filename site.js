const navigationLinks = Array.from(
  document.querySelectorAll('nav a[href^="#"]')
);

const navigationTargets = navigationLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

let currentSectionId;
const setCurrentSection = (id) => {
  if (id === currentSectionId) {
    return;
  }

  currentSectionId = id;
  let currentLink;

  navigationLinks.forEach((link) => {
    if (link.getAttribute("href") === `#${id}`) {
      link.setAttribute("aria-current", "true");
      currentLink = link;
    } else {
      link.removeAttribute("aria-current");
    }
  });

  const navigation = currentLink?.closest("nav");
  if (navigation && navigation.scrollWidth > navigation.clientWidth) {
    const centeredPosition =
      currentLink.offsetLeft - (navigation.clientWidth - currentLink.offsetWidth) / 2;
    navigation.scrollTo({
      left: centeredPosition,
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "auto"
        : "smooth",
    });
  }
};

const updateCurrentSection = () => {
  if (!navigationTargets.length) {
    return;
  }

  const navigationHeight = Number.parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue("--nav-height")
  );
  const activationLine = (Number.isFinite(navigationHeight) ? navigationHeight : 0) + 1;
  let currentTarget = navigationTargets[0];

  navigationTargets.forEach((target) => {
    if (target.getBoundingClientRect().top <= activationLine) {
      currentTarget = target;
    }
  });

  const pageBottom = window.scrollY + window.innerHeight;
  if (pageBottom >= document.documentElement.scrollHeight - 1) {
    currentTarget = navigationTargets[navigationTargets.length - 1];
  }

  setCurrentSection(currentTarget.id);
};

let updateFrame;
const requestCurrentSectionUpdate = () => {
  if (updateFrame) {
    return;
  }

  updateFrame = requestAnimationFrame(() => {
    updateCurrentSection();
    updateFrame = undefined;
  });
};

window.addEventListener("scroll", requestCurrentSectionUpdate, { passive: true });
window.addEventListener("resize", requestCurrentSectionUpdate);
window.addEventListener("hashchange", requestCurrentSectionUpdate);
updateCurrentSection();
