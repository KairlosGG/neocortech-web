(function(){
var ix=document.getElementById('ix');if(!ix)return;
var items=[].slice.call(ix.querySelectorAll('.ix-it'));
var wide=window.matchMedia('(min-width: 901px)');
var fine=window.matchMedia('(hover: hover) and (pointer: fine)');
function row(it){return it.querySelector('.ix-row');}
function visible(){return items.filter(function(it){return !it.classList.contains('off');});}
function setOpen(target){
  if(target&&current()===target)return;
  items.forEach(function(it){var on=it===target;row(it).setAttribute('aria-expanded',String(on));it.querySelector('.ix-panel').classList.toggle('on',on);});
}
function current(){for(var i=0;i<items.length;i++){if(row(items[i]).getAttribute('aria-expanded')==='true')return items[i];}return null;}
function refresh(){if(window.ScrollTrigger)window.ScrollTrigger.refresh();}
var hoverT=null;
function headerOff(){var n=document.getElementById('nav');var b=(n&&!n.classList.contains('hide'))?n.getBoundingClientRect().bottom:0;return Math.max(0,b)+8;}
function jump(y,smooth){
  var rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(window.__lenis){if(window.__lenis.resize)window.__lenis.resize();window.__lenis.scrollTo(y,{immediate:!smooth||rm,force:true});}
  else window.scrollTo({top:y,behavior:(smooth&&!rm)?'smooth':'auto'});
}
function keepInView(r,before){
  var after=r.getBoundingClientRect().top;
  if(Math.abs(after-before)>1)jump(window.scrollY+(after-before),false);
  var off=headerOff();
  if(before<off||before>innerHeight*.5){var t=r.getBoundingClientRect().top;jump(window.scrollY+t-off,true);}
}
items.forEach(function(it){
  var r=row(it);
  r.addEventListener('click',function(){
    if(wide.matches){setOpen(it);return;}
    var was=r.getAttribute('aria-expanded')==='true';
    /* fase 2: al cerrarse otra ficha más arriba, la fila pulsada no debe salir disparada.
       Se compensa el desplazamiento al momento y, si la fila queda bajo la cabecera o en la mitad baja, se lleva arriba. */
    var before=r.getBoundingClientRect().top;
    setOpen(was?null:it);refresh();
    if(!was)keepInView(r,before);
  });
  r.addEventListener('mouseenter',function(){
    if(!wide.matches||!fine.matches)return;
    clearTimeout(hoverT);
    /* fase 1: si ya hay un panel abierto se cambia al momento (sin parpadeo al recorrer la lista) */
    if(current())setOpen(it);else hoverT=setTimeout(function(){setOpen(it);},90);
  });
  r.addEventListener('mouseleave',function(){clearTimeout(hoverT);});
  r.addEventListener('focus',function(){if(wide.matches)setOpen(it);});
  r.addEventListener('keydown',function(e){
    var v=visible(),i=v.indexOf(it),n=null;
    if(e.key==='ArrowDown')n=v[Math.min(i+1,v.length-1)];
    else if(e.key==='ArrowUp')n=v[Math.max(i-1,0)];
    else if(e.key==='Home')n=v[0];
    else if(e.key==='End')n=v[v.length-1];
    if(n){e.preventDefault();row(n).focus();}
  });
  var dots=it.querySelectorAll('.ix-dots button'),imgs=it.querySelectorAll('.ix-media img');
  [].forEach.call(dots,function(d,j){
    d.addEventListener('click',function(){
      [].forEach.call(imgs,function(im,k){im.classList.toggle('on',k===j);if(k===j)im.removeAttribute('aria-hidden');else im.setAttribute('aria-hidden','true');});
      [].forEach.call(dots,function(o,k){if(k===j)o.setAttribute('aria-current','true');else o.removeAttribute('aria-current');});
    });
  });
});
[].forEach.call(document.querySelectorAll('.ixf'),function(b,_,all){
  b.addEventListener('click',function(){
    var f=b.getAttribute('data-f');
    [].forEach.call(document.querySelectorAll('.ixf'),function(o){o.setAttribute('aria-pressed',String(o===b));});
    items.forEach(function(it){var c=(it.getAttribute('data-cats')||'').split(' ');it.classList.toggle('off',f!=='all'&&c.indexOf(f)<0);});
    var v=visible();ix.style.setProperty('--n',String(Math.max(v.length,1)));
    /* fase 2: aviso discreto del número de resultados para lector de pantalla */
    var live=document.getElementById('ixLive');
    if(live){var lab=(b.querySelector('[data-i18n]')||b).textContent.trim();live.textContent=lab+': '+v.length+' '+(v.length===1?NCT('proyecto','project'):NCT('proyectos','projects'));}
    var cur=current();
    if(wide.matches){if(!cur||cur.classList.contains('off'))setOpen(v[0]||null);}
    else if(cur&&cur.classList.contains('off'))setOpen(null);
    refresh();
  });
});
if(!wide.matches)setOpen(null);
var onChange=function(){if(wide.matches&&!current())setOpen(visible()[0]||null);refresh();};
if(wide.addEventListener)wide.addEventListener('change',onChange);else if(wide.addListener)wide.addListener(onChange);
})();
