/* fase 2 · accesibilidad y UX */
(function(){
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
/* la distancia bajo la cabecera la fija scroll-padding-top (CSS); Lenis ya la tiene en cuenta */
function pad(){return parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop)||0;}
/* ir a un ancla: desplaza (con Lenis si está), mueve el foco al destino y actualiza la URL */
window.__goTo=function(el,hash,push){
  if(!el.hasAttribute('tabindex')&&!/^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(el.tagName))el.setAttribute('tabindex','-1');
  var done=function(){try{el.focus({preventScroll:true});}catch(e){}};
  if(window.__lenis)window.__lenis.scrollTo(el,{offset:0,immediate:RM,onComplete:done});
  else{el.scrollIntoView({behavior:RM?'auto':'smooth'});done();}
  if(push&&hash&&location.hash!==hash){try{history.pushState(null,'',hash);}catch(e){}}
};
/* al cargar con #seccion (p. ej. tras cambiar de idioma): recolocar cuando ya están medidas las secciones */
if(location.hash.length>1){
  var t=document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if(t){var fix=function(){var y=t.getBoundingClientRect().top;if(Math.abs(y-pad())>4){
      if(window.__lenis)window.__lenis.scrollTo(t,{offset:0,immediate:true,force:true});else window.scrollTo(0,scrollY+y-pad());}};
    addEventListener('load',function(){setTimeout(fix,80);setTimeout(fix,700);});}
}
/* «Atrás»/«Adelante» entre anclas */
addEventListener('popstate',function(){var h=location.hash,el=h.length>1&&document.getElementById(decodeURIComponent(h.slice(1)));if(el)window.__goTo(el,h,false);});
/* el teclado no espera al revelado: si el foco cae en algo que aún está apareciendo, se muestra ya */
document.addEventListener('focusin',function(e){var r=e.target&&e.target.closest&&e.target.closest('.rvx');
  if(r&&parseFloat(getComputedStyle(r).opacity)<1){if(window.gsap){gsap.killTweensOf(r);gsap.set(r,{autoAlpha:1,y:0});}else{r.style.opacity=1;r.style.transform='none';}}});
})();
