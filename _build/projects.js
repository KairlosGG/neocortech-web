(function(){
var ix=document.getElementById('ix');if(!ix)return;
var items=[].slice.call(ix.querySelectorAll('.ix-it'));
var wide=window.matchMedia('(min-width: 901px)');
var fine=window.matchMedia('(hover: hover) and (pointer: fine)');
function row(it){return it.querySelector('.ix-row');}
function visible(){return items.filter(function(it){return !it.classList.contains('off');});}
function setOpen(target){
  items.forEach(function(it){var on=it===target;row(it).setAttribute('aria-expanded',String(on));it.querySelector('.ix-panel').classList.toggle('on',on);});
}
function current(){for(var i=0;i<items.length;i++){if(row(items[i]).getAttribute('aria-expanded')==='true')return items[i];}return null;}
function refresh(){if(window.ScrollTrigger)window.ScrollTrigger.refresh();}
var hoverT=null;
items.forEach(function(it){
  var r=row(it);
  r.addEventListener('click',function(){
    if(wide.matches){setOpen(it);return;}
    var was=r.getAttribute('aria-expanded')==='true';
    setOpen(was?null:it);refresh();
  });
  r.addEventListener('mouseenter',function(){
    if(!wide.matches||!fine.matches)return;
    clearTimeout(hoverT);hoverT=setTimeout(function(){setOpen(it);},90);
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
      [].forEach.call(imgs,function(im,k){im.classList.toggle('on',k===j);});
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
