(function(){
"use strict";
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches, FINE=matchMedia('(pointer:fine)').matches;
var hasGSAP=!!window.gsap;
if(hasGSAP&&window.ScrollTrigger){gsap.registerPlugin(ScrollTrigger);}


/* ember field */
(function(){var c=document.getElementById('field');if(!c)return;var x=c.getContext('2d'),W,H,DPR,parts=[],mouse={x:-999,y:-999};
function size(){DPR=1;W=c.width=innerWidth*DPR;H=c.height=innerHeight*DPR;c.style.width=innerWidth+'px';c.style.height=innerHeight+'px';}
size();addEventListener('resize',size);
function sprite(c0,c1,c2){var s=document.createElement('canvas');s.width=s.height=64;var g2=s.getContext('2d');var g=g2.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,c0);g.addColorStop(.5,c1);g.addColorStop(1,c2);g2.fillStyle=g;g2.fillRect(0,0,64,64);return s;}
var SPR_G=sprite('rgba(240,216,150,1)','rgba(201,162,75,.5)','rgba(125,95,38,0)');
var SPR_S=sprite('rgba(127,180,232,1)','rgba(91,143,198,.5)','rgba(91,143,198,0)');
var N=RM?0:Math.min(88,Math.floor(innerWidth/16));
for(var i=0;i<N;i++)parts.push({x:Math.random()*W,y:Math.random()*H,r:(Math.random()*1.6+.5)*DPR,vx:(Math.random()-.5)*.12*DPR,vy:(-Math.random()*.32-.05)*DPR,a:Math.random()*.5+.15,ph:Math.random()*6.28,sp:Math.random()*.02+.005,sap:Math.random()<.28});
if(FINE)addEventListener('pointermove',function(e){mouse.x=e.clientX*DPR;mouse.y=e.clientY*DPR;},{passive:true});
var sv=0,ls=0;addEventListener('scroll',function(){sv=Math.min(Math.abs(scrollY-ls),60);ls=scrollY;},{passive:true});
function f(){x.clearRect(0,0,W,H);x.globalCompositeOperation='lighter';
for(var i=0;i<parts.length;i++){var p=parts[i];p.ph+=p.sp;p.x+=p.vx+Math.sin(p.ph)*.18*DPR;p.y+=p.vy-(sv*.004*DPR);
var dx=p.x-mouse.x,dy=p.y-mouse.y,d2=dx*dx+dy*dy,rad=120*DPR;if(d2<rad*rad){var d=Math.sqrt(d2)||1,fo=(1-d/rad)*1.4;p.x+=dx/d*fo;p.y+=dy/d*fo;}
if(p.y<-10){p.y=H+10;p.x=Math.random()*W;}if(p.x<-10)p.x=W+10;if(p.x>W+10)p.x=-10;
var tw=p.a*(.6+.4*Math.sin(p.ph*2));var R4=p.r*4;
x.globalAlpha=tw<0?0:tw>1?1:tw;x.drawImage(p.sap?SPR_S:SPR_G,p.x-R4,p.y-R4,R4*2,R4*2);}
x.globalAlpha=1;sv*=.9;x.globalCompositeOperation='source-over';if(active)requestAnimationFrame(f);else{x.clearRect(0,0,W,H);running=false;}}
/* fase 1: solo en el hero y el pie; en pausa el resto del tiempo */
var active=false,running=false,vis={};
c.style.transition='opacity .6s';c.style.opacity=0;
function setActive(v){c.style.opacity=v?1:0;v=v&&!document.hidden;active=v;if(v&&!running&&!RM){running=true;requestAnimationFrame(f);}}
if(!RM&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){vis[e.target.id]=e.isIntersecting;});setActive(!!(vis.hero||vis.contacto));},{threshold:.12});
['hero','contacto'].forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el);});
document.addEventListener('visibilitychange',function(){setActive(!!(vis.hero||vis.contacto));});}
})();

/* black box */
(function(){var box=document.getElementById('bb'),cv=document.getElementById('bbc');if(!box||!cv)return;
var x=cv.getContext('2d'),W,H,DPR,reveal=0,target=0,held=false;
var stateEl=document.getElementById('bbState'),hintEl=document.getElementById('bbHint');
if(!FINE&&hintEl)hintEl.textContent=NCT('toca y mantén pulsada la caja para abrirla','tap and hold the box to open it');
var nodes=[{x:.10,y:.5,l:NCT('PETICIÓN','REQUEST'),t:'in'},{x:.32,y:.27,l:NCT('PERCEPCIÓN','PERCEPTION'),t:'p'},{x:.32,y:.73,l:NCT('CONTEXTO·RAG','CONTEXT·RAG'),t:'p'},{x:.55,y:.5,l:NCT('RAZONAMIENTO','REASONING'),t:'r'},{x:.74,y:.29,l:NCT('POLÍTICA·ISO 42001','POLICY·ISO 42001'),t:'pol'},{x:.74,y:.71,l:NCT('VERIFICACIÓN','VERIFICATION'),t:'pol'},{x:.90,y:.5,l:NCT('ACCIÓN','ACTION'),t:'out'}];
var edges=[[0,1],[0,2],[1,3],[2,3],[3,4],[3,5],[4,6],[5,6]];
function size(){DPR=Math.min(devicePixelRatio||1,2);var r=box.getBoundingClientRect();W=cv.width=r.width*DPR;H=cv.height=r.height*DPR;}
size();addEventListener('resize',function(){size();draw();});
function pos(n){return{x:n.x*W,y:n.y*H};}
function col(t,a){if(t==='pol')return'rgba(240,216,150,'+a+')';if(t==='out')return'rgba(201,162,75,'+a+')';if(t==='in')return'rgba(236,231,218,'+a+')';if(t==='r')return'rgba(127,180,232,'+a+')';return'rgba(91,143,198,'+a+')';}
function draw(){x.clearRect(0,0,W,H);x.lineWidth=1.2*DPR;
for(var i=0;i<edges.length;i++){var prog=Math.max(0,Math.min(1,(reveal-.05)*1.4-i*.04));if(prog<=0)continue;
var a=pos(nodes[edges[i][0]]),b=pos(nodes[edges[i][1]]);x.strokeStyle='rgba(201,162,75,'+(.28*prog)+')';x.beginPath();x.moveTo(a.x,a.y);x.lineTo(a.x+(b.x-a.x)*prog,a.y+(b.y-a.y)*prog);x.stroke();
if(prog>=1&&reveal>.6){var tt=(performance.now()/900+i*.2)%1,px=a.x+(b.x-a.x)*tt,py=a.y+(b.y-a.y)*tt;x.fillStyle='rgba(240,216,150,'+(reveal*.9)+')';x.beginPath();x.arc(px,py,2.2*DPR,0,6.28);x.fill();}}
for(var j=0;j<nodes.length;j++){var p=pos(nodes[j]),ap=Math.max(0,Math.min(1,(reveal-.02)*1.6-j*.05));if(ap<=0)continue;
var rr=(nodes[j].t==='r'?7:5)*DPR*ap,g=x.createRadialGradient(p.x,p.y,0,p.x,p.y,rr*3);g.addColorStop(0,col(nodes[j].t,.9*ap));g.addColorStop(1,col(nodes[j].t,0));
x.fillStyle=g;x.beginPath();x.arc(p.x,p.y,rr*3,0,6.28);x.fill();x.fillStyle=col(nodes[j].t,ap);x.beginPath();x.arc(p.x,p.y,rr,0,6.28);x.fill();
if(reveal>.45){x.fillStyle='rgba(236,231,218,'+((reveal-.45)*1.6*ap)+')';x.font=(9.5*DPR)+'px "Cinzel",serif';x.textAlign='center';x.fillText(nodes[j].l,p.x,p.y-rr-7*DPR);}}
if(reveal<1){x.fillStyle='rgba(8,16,25,'+(.62*(1-reveal))+')';x.fillRect(0,0,W,H);
if(reveal<.5){x.fillStyle='rgba(126,146,166,'+(.5*(1-reveal*2))+')';x.font=(46*DPR)+'px "Cinzel",serif';x.textAlign='center';x.fillText('?',W*.5,H*.5+16*DPR);}}}
var bbRun=false,bbVis=false,bbSt='',bbHo=-1;
function bbOn(){return bbVis&&!document.hidden;}
function kick(){if(!bbRun&&bbOn()){bbRun=true;requestAnimationFrame(loop);}}
var kb=false;if(!RM){box.setAttribute('tabindex','0');box.setAttribute('role','button');box.setAttribute('aria-pressed','false');
box.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();kb=!kb;box.setAttribute('aria-pressed',String(kb));}});
box.addEventListener('blur',function(){kb=false;box.setAttribute('aria-pressed','false');});}
function loop(){target=(held||kb)?1:((box.matches(':hover')||document.activeElement===box)?Math.max(target,.62):0);reveal+=(target-reveal)*.08;
if(Math.abs(target-reveal)<.002)reveal=target;
var st=reveal>.85?'AUDITABLE':reveal>.4?NCT('ABRIENDO…','OPENING…'):NCT('OPACO','OPAQUE');if(stateEl&&st!==bbSt){stateEl.textContent=st;bbSt=st;}
var ho=reveal>.3?0:1;if(hintEl&&ho!==bbHo){hintEl.style.opacity=ho;bbHo=ho;}draw();
if(bbOn()&&(reveal!==target||reveal>.6))requestAnimationFrame(loop);else bbRun=false;}
box.addEventListener('pointermove',function(e){var r=box.getBoundingClientRect(),my=(e.clientY-r.top)/r.height;if(!held)target=Math.max(target,.5+(1-Math.abs(my-.5))*.4);});
box.addEventListener('pointerdown',function(){held=true;});addEventListener('pointerup',function(){held=false;});
box.addEventListener('pointerleave',function(){if(!held)target=0;});
box.addEventListener('click',function(){target=1;held=true;setTimeout(function(){held=false;},1400);});
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){if(!bbRun)draw();});
if(RM){reveal=1;draw();}else{draw();if(stateEl){bbSt=NCT('OPACO','OPAQUE');stateEl.textContent=bbSt;}
['pointerenter','pointermove','pointerdown','pointerleave','click','keydown','focus','blur'].forEach(function(n){box.addEventListener(n,kick);});
addEventListener('pointerup',kick);document.addEventListener('visibilitychange',kick);
if('IntersectionObserver' in window)new IntersectionObserver(function(e){bbVis=e[0].isIntersecting;kick();}).observe(box);else{bbVis=true;kick();}}})();

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

/* loader — fase 1: ~0,75 s solo en la primera visita de la sesión, sin contador; después, nada */
(function(){var ld=document.getElementById('loader'),cur=document.querySelector('.curtain');
var seen=false;try{seen=sessionStorage.getItem('nc_seen')==='1';sessionStorage.setItem('nc_seen','1');}catch(e){}
if(RM||!hasGSAP){if(ld)ld.style.display='none';if(cur)cur.style.display='none';heroIn();return;}
if(seen||!ld){if(ld)ld.style.display='none';gsap.set('.curtain i',{yPercent:-100});heroIn();return;}
gsap.timeline()
  .fromTo('#loader .mk',{autoAlpha:0,scale:.86},{autoAlpha:1,scale:1,duration:.28,ease:'expo.out'})
  .to(ld,{autoAlpha:0,duration:.2,onComplete:function(){ld.style.display='none';}})
  .to('.curtain i',{yPercent:-100,duration:.4,ease:'expo.inOut',stagger:.02},'<')
  .add(heroIn,'-=.3');})();

/* cortina de navegación — la salida cubre subiendo; bfcache; prefetch al hover */
(function(){
var cover=false;
function internal(a){
  if(!a||a.target==='_blank'||a.hasAttribute('download'))return null;
  var href=a.getAttribute('href');if(!href)return null;
  var u;try{u=new URL(a.href,location.href);}catch(e){return null;}
  if(u.origin!==location.origin)return null;
  if(u.protocol!=='http:'&&u.protocol!=='https:')return null;
  if(u.pathname===location.pathname&&u.hash)return null;
  return u;
}
addEventListener('pageshow',function(e){if(e.persisted){cover=false;if(ldEl())ldEl().style.display='none';
  if(window.gsap){gsap.set('.curtain i',{yPercent:-100});}else{document.querySelectorAll('.curtain i').forEach(function(p){p.style.transform='translateY(-100%)';});}}});
function ldEl(){return document.getElementById('loader');}
if(RM||!hasGSAP)return;
document.addEventListener('click',function(e){
  if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
  var a=e.target&&e.target.closest?e.target.closest('a[href]'):null;
  var u=internal(a);if(!u||cover)return;
  if(u.pathname===location.pathname&&!u.hash){e.preventDefault();if(window.__lenis)window.__lenis.scrollTo(0);else window.scrollTo({top:0,behavior:'smooth'});return;}
  e.preventDefault();cover=true;
  var ps=document.querySelectorAll('.curtain i');
  gsap.set(ps,{yPercent:100});
  gsap.to(ps,{yPercent:0,duration:.42,ease:'expo.in',stagger:.02,onComplete:function(){location.href=u.href;}});
});
document.addEventListener('pointerenter',function(e){
  var t=e.target;if(!t||!t.closest)return;
  var u=internal(t.closest('a[href]'));if(!u)return;
  if(u.pathname===location.pathname)return;
  if(document.querySelector('link[rel="prefetch"][href="'+u.href+'"]'))return;
  var l=document.createElement('link');l.rel='prefetch';l.href=u.href;document.head.appendChild(l);
},true);
})();

function heroIn(){var h1=document.getElementById('heroH1');
if(!hasGSAP||RM){document.querySelectorAll('.rvx').forEach(function(e){e.style.opacity=1;e.style.transform='none';});if(h1)h1.querySelectorAll('.line-mask>span').forEach(function(s){s.style.transform='none';});initScroll();return;}
var tl=gsap.timeline();
tl.from('#heroH1 .line-mask>span',{yPercent:118,duration:1.05,ease:'power4.out',stagger:.08})
.fromTo('.hero .tagrow',{y:20,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.7')
.fromTo('.hero-foot .intro',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.5')
.fromTo('.hero-foot .meta',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.6')
.fromTo('.hero-cta',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.6')
.fromTo('.scrollcue',{autoAlpha:0},{autoAlpha:1,duration:.6},'-=.4');
initScroll();}

function initScroll(){var lenis=null;
if(window.Lenis&&!RM){lenis=new Lenis({duration:1.1,easing:function(t){return Math.min(1,1.001-Math.pow(2,-10*t));},smoothWheel:true});
(function(){var id=0,idle=0;
function tick(t){id=0;lenis.raf(t);var busy=lenis.isScrolling==='smooth'||(lenis.animate&&lenis.animate.isRunning);idle=busy?0:idle+1;if(idle<20&&!document.hidden)id=requestAnimationFrame(tick);}
function wake(){if(!id&&!document.hidden){lenis.time=0;idle=0;id=requestAnimationFrame(tick);}}
var st0=lenis.scrollTo;lenis.scrollTo=function(){var r=st0.apply(lenis,arguments);wake();return r;};
addEventListener('wheel',wake,{passive:true,capture:true});document.addEventListener('visibilitychange',wake);wake();})();if(hasGSAP&&window.ScrollTrigger){lenis.on('scroll',ScrollTrigger.update);}window.__lenis=lenis;}
document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var el=document.getElementById(id.slice(1));if(!el)return;e.preventDefault();if(window.__setMenu)window.__setMenu(false,true);if(lenis)lenis.start();window.__goTo(el,id,true);});});

if(!hasGSAP||RM){document.querySelectorAll('.rvx').forEach(function(e){e.style.opacity=1;e.style.transform='none';});var cn=document.getElementById('cinema');if(cn)cn.classList.add('still');
  var tfb=document.getElementById('toTopFloat'),btb=document.getElementById('toTop');
  function go(){if(window.__lenis)window.__lenis.scrollTo(0);else window.scrollTo({top:0,behavior:'smooth'});}
  if(btb)btb.addEventListener('click',go);if(tfb){tfb.addEventListener('click',go);addEventListener('scroll',function(){tfb.classList.toggle('show',scrollY>innerHeight*1.3);},{passive:true});}
  return;}

/* fase 1: un solo revelado sobrio para todo (misma curva y duración), una vez */
var EASE='expo.out';
ScrollTrigger.batch(gsap.utils.toArray('.rvx').filter(function(el){return !el.closest('.hero');}),{start:'top 90%',once:true,
  onEnter:function(b){gsap.to(b,{autoAlpha:1,y:0,duration:.7,ease:EASE,stagger:.05,overwrite:true});}});


/* retrato — fase 1: el vídeo solo se pide al acercarse y solo en escritorio con puntero fino;
   en móvil y con movimiento reducido se queda el póster (imagen) */
var cine=document.getElementById('cinema'),cinevid=document.getElementById('cinevid'),cinebar=document.getElementById('cinebar'),scrubhint=document.getElementById('scrubhint');
if(cine){
  gsap.fromTo(cine,{clipPath:'inset(7% 3% 7% 3% round 20px)'},{clipPath:'inset(0% 0% 0% 0% round 20px)',duration:1.1,ease:EASE,scrollTrigger:{trigger:cine,start:'top 85%',once:true}});
  var canScrub=!!cinevid&&FINE&&matchMedia('(min-width:901px)').matches;
  if(canScrub){
    var want=0,loaded=false;
    var loadVid=function(){if(loaded)return;loaded=true;cinevid.preload='auto';cinevid.load();};
    if('IntersectionObserver' in window){var vio=new IntersectionObserver(function(es){if(es[0].isIntersecting){loadVid();vio.disconnect();}},{rootMargin:'700px 0px'});vio.observe(cine);}else loadVid();
    var seek=function(){var d=cinevid.duration;if(!d||!isFinite(d)||cinevid.readyState<1||cinevid.seeking)return;
      var t=Math.max(0,Math.min(d-0.05,want*d));if(Math.abs(t-cinevid.currentTime)>0.03){try{cinevid.currentTime=t;}catch(e){}}};
    cinevid.addEventListener('loadedmetadata',seek);cinevid.addEventListener('seeked',seek);
    cinevid.addEventListener('loadeddata',function(){cinevid.classList.add('ready');seek();});
    ScrollTrigger.create({trigger:cine,start:'top 80%',end:'bottom 16%',onUpdate:function(s){want=s.progress;seek();
      if(cinebar)cinebar.style.width=(s.progress*100)+'%';
      if(scrubhint)scrubhint.style.opacity=s.progress>0.02?0:1;}});
    gsap.fromTo('#cinema video,#cinema .poster',{scale:1.06},{scale:1,ease:'none',scrollTrigger:{trigger:cine,start:'top bottom',end:'bottom top',scrub:true}});
  } else cine.classList.add('still');
}

/* Venn: estático desde la fase 1 */

/* tesis — carrusel horizontal nativo (drag + snap + fases), sin pin */
var track=document.getElementById('htrack'),prog=document.getElementById('hprog');
var dots=Array.prototype.slice.call(document.querySelectorAll('.hdot'));
/* sello del doctorado — se estampa una vez al recorrer las cinco fases */
var sealEl=document.getElementById('thSeal'),sealDone=false;
function stampSeal(){
  if(sealDone||!sealEl)return;sealDone=true;
  var hh=document.querySelector('.hhint');
  if(hh){hh.textContent=NCT('✦ recorrido completo','✦ path complete');hh.style.color='var(--gold-bright)';}
  if(RM||!hasGSAP){if(innerWidth<=820)sealEl.style.opacity=1;return;}
  gsap.fromTo(sealEl,{autoAlpha:0},{autoAlpha:1,duration:.6,ease:EASE});
  if(innerWidth>820){gsap.to(sealEl,{autoAlpha:0,y:-14,duration:.6,delay:2.7,ease:'power2.in'});}
}
if(track&&innerWidth>820){
  var panels=gsap.utils.toArray('#htrack .hpanel');
  var maxS=function(){return Math.max(1,track.scrollWidth-track.clientWidth);};
  function focusPanels(){var tr=track.getBoundingClientRect();panels.forEach(function(pl){var r=pl.getBoundingClientRect();var dist=Math.abs(r.left-tr.left);/* fase 1: foco en el borde izquierdo (retícula) */var k=Math.max(0,1-dist/(tr.width*0.85));gsap.set(pl,{scale:0.93+0.07*k,opacity:0.45+0.55*k});});}
  function trackUpdate(){var p=track.scrollLeft/maxS();if(prog)prog.style.width=(Math.min(1,p)*100)+'%';
    var idx=Math.round(Math.min(1,p)*(panels.length-1));dots.forEach(function(d,i){d.classList.toggle('active',i===idx);});panels.forEach(function(pl,i){pl.classList.toggle('active',i===idx);});
    if(p>=0.98)stampSeal();focusPanels();}
  track.addEventListener('scroll',trackUpdate,{passive:true});
  addEventListener('resize',trackUpdate);
  dots.forEach(function(d,i){d.addEventListener('click',function(){track.scrollTo({left:i/(panels.length-1)*maxS(),behavior:'smooth'});});});
  var drag=false,sx=0,sl=0;
  track.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;drag=true;sx=e.clientX;sl=track.scrollLeft;track.classList.add('dragging');track.setPointerCapture(e.pointerId);});
  track.addEventListener('pointermove',function(e){if(!drag)return;track.scrollLeft=sl-(e.clientX-sx);});
  addEventListener('pointerup',function(){if(drag){drag=false;track.classList.remove('dragging');}});
  trackUpdate();
}else if(track&&'IntersectionObserver' in window){
  var lastPanel=document.querySelectorAll('#htrack .hpanel');lastPanel=lastPanel[lastPanel.length-1];
  if(lastPanel){var sio=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){stampSeal();sio.disconnect();}});},{threshold:.55});sio.observe(lastPanel);}
}

/* nav hide + progress + active + back-to-top float */
var nav=document.getElementById('nav'),last=0,tf=document.getElementById('toTopFloat');
ScrollTrigger.create({start:0,end:'max',onUpdate:function(s){var y=s.scroll();if(y>140&&y>last)nav.classList.add('hide');else nav.classList.remove('hide');nav.classList.toggle('solid',y>40);last=y;if(tf)tf.classList.toggle('show',y>innerHeight*1.3);}});
gsap.to('#prog',{scaleX:1,ease:'none',scrollTrigger:{start:0,end:'max',scrub:.3}});
function toTopGo(){if(window.__lenis)window.__lenis.scrollTo(0,{duration:1.2});else window.scrollTo({top:0,behavior:'smooth'});}
var bt=document.getElementById('toTop');if(bt)bt.addEventListener('click',toTopGo);if(tf)tf.addEventListener('click',toTopGo);

ScrollTrigger.refresh();setTimeout(function(){ScrollTrigger.refresh();},450);}


})();;
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
})();;
(function(){
var ix=document.getElementById('ix');if(!ix)return;
var items=[].slice.call(ix.querySelectorAll('.ix-it'));
var wide=window.matchMedia('(min-width: 901px)');
var fine=window.matchMedia('(hover: hover) and (pointer: fine)');
function row(it){return it.querySelector('.ix-row');}
function visible(){return items.filter(function(it){return !it.classList.contains('off');});}
/* fase 4: las imágenes de los paneles cerrados no se descargan hasta que se van a mostrar.
   Se hidratan (data-srcset/data-src -> srcset/src) al pasar o enfocar la fila, con sus dos vecinas por arriba y por abajo,
   al pulsarla y cuando el índice queda cerca de la pantalla (el panel abierto y sus vecinas). */
function hydrate(it){if(!it||it.__h)return;it.__h=1;
  [].forEach.call(it.querySelectorAll('img[data-src]'),function(im){if(im.dataset.srcset){im.srcset=im.dataset.srcset;im.removeAttribute('data-srcset');}im.src=im.dataset.src;im.removeAttribute('data-src');});}
function warm(it){hydrate(it);var v=visible(),i=v.indexOf(it);if(i<0)return;for(var d=1;d<=2;d++){hydrate(v[i+d]);hydrate(v[i-d]);}}
function setOpen(target){
  if(target)hydrate(target);
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
  r.addEventListener('pointerdown',function(){hydrate(it);},{passive:true});
  /* QA: solo con movimiento real del ratón; al hacer scroll con el puntero quieto no cambia la ficha */
  r.addEventListener('pointermove',function(e){
    if(e.pointerType!=='mouse'||!wide.matches||!fine.matches||current()===it)return;
    warm(it);
    clearTimeout(hoverT);
    /* fase 1: si ya hay un panel abierto se cambia al momento (sin parpadeo al recorrer la lista) */
    if(current())setOpen(it);else hoverT=setTimeout(function(){setOpen(it);},90);
  });
  r.addEventListener('mouseleave',function(){clearTimeout(hoverT);});
  r.addEventListener('focus',function(){if(wide.matches){warm(it);setOpen(it);}});
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
ix.classList.add('ix-ready');
if('IntersectionObserver' in window){var nio=new IntersectionObserver(function(es){if(es[0].isIntersecting&&wide.matches){warm(current()||visible()[0]);nio.disconnect();}},{rootMargin:'300px 0px'});nio.observe(ix);}
/* fase 4: en escritorio el panel es fijo (sticky). Si un panel mide más que la ventana (LiVRe), se fija por abajo:
   baja con la página hasta que se ve su final y ahí se queda, así el texto se lee entero sin perder el sticky. */
function fitSticky(){
  items.forEach(function(it){var p=it.querySelector('.ix-panel');p.style.top='';
    if(!wide.matches)return;
    var base=parseFloat(getComputedStyle(p).top)||96,h=p.offsetHeight;
    if(h>innerHeight-base-24)p.style.top=(innerHeight-h-24)+'px';});
}
fitSticky();addEventListener('resize',fitSticky);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitSticky);
if('ResizeObserver' in window){var fsT=0,ro=new ResizeObserver(function(){cancelAnimationFrame(fsT);fsT=requestAnimationFrame(fitSticky);});items.forEach(function(it){ro.observe(it.querySelector('.ix-panel'));});}
var onChange=function(){if(wide.matches&&!current())setOpen(visible()[0]||null);refresh();};
if(wide.addEventListener)wide.addEventListener('change',onChange);else if(wide.addListener)wide.addListener(onChange);
})();
