/* overlay menu — fase 2: cerrado es inerte; abierto, el foco entra, queda atrapado (botón + menú), el resto de la página queda inerte y Escape devuelve el foco al botón */
(function(){var btn=document.getElementById('menuBtn'),ov=document.getElementById('overlay'),txt=document.getElementById('menuTxt');var open=false;
function bg(o){[].forEach.call(document.body.children,function(el){if(el===ov||el.id==='nav'||el.tagName==='SCRIPT')return;if(o)el.setAttribute('inert','');else el.removeAttribute('inert');});}
function focusables(){return [btn].concat([].slice.call(ov.querySelectorAll('a[href],button')).filter(function(e){return e.getClientRects().length;}));}
function setOpen(o,keepFocus){if(o===open)return;open=o;ov.classList.toggle('open',o);if(o)ov.removeAttribute('inert');else ov.setAttribute('inert','');bg(o);
document.body.classList.toggle('menu-open',o);btn.setAttribute('aria-expanded',String(o));txt.textContent=o?NCT('Cerrar','Close'):NCT('Índice','Index');
if(window.__lenis){if(o)window.__lenis.stop();else window.__lenis.start();}
if(o){var f=ov.querySelector('a[href]');var tryF=function(n){if(!f||!open)return;f.focus({preventScroll:true});if(document.activeElement!==f&&n<10)requestAnimationFrame(function(){tryF(n+1);});};tryF(0);}
else if(!keepFocus&&(ov.contains(document.activeElement)||document.activeElement===document.body||!document.activeElement))btn.focus({preventScroll:true});
if(hasGSAP&&!RM){if(o){gsap.to(ov,{clipPath:'inset(0 0 0% 0)',duration:.7,ease:'power4.inOut'});gsap.fromTo('#ovNav a',{y:40,opacity:0},{y:0,opacity:1,duration:.6,stagger:.06,delay:.12,ease:'power3.out'});gsap.fromTo('.ov-pages,.ov-side>*',{y:20,opacity:0},{y:0,opacity:1,duration:.5,stagger:.05,delay:.28,ease:'power3.out'});}
else{gsap.to(ov,{clipPath:'inset(0 0 100% 0)',duration:.55,ease:'power4.inOut'});}}
else{ov.style.clipPath=o?'inset(0 0 0% 0)':'inset(0 0 100% 0)';}}
btn.addEventListener('click',function(){setOpen(!open);});
ov.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(){setOpen(false,true);});});
addEventListener('keydown',function(e){if(!open)return;
  if(e.key==='Escape'){e.preventDefault();setOpen(false);btn.focus({preventScroll:true});return;}
  if(e.key==='Tab'){var f=focusables(),i=f.indexOf(document.activeElement);
    if(e.shiftKey&&i<=0){e.preventDefault();f[f.length-1].focus();}
    else if(!e.shiftKey&&(i===f.length-1||i<0)){e.preventDefault();f[0].focus();}}});
window.__setMenu=setOpen;})();
