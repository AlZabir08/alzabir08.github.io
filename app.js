const menuButton=document.querySelector('#menu-toggle');
function revealPortfolioEntry(){
 let id;
 try{id=decodeURIComponent(window.location.hash.slice(1));}catch{return;}
 if(!id)return;
 const entry=document.getElementById(id);
 const details=entry?.querySelector('details.entry-details');
 if(details)details.open=true;
}
window.addEventListener('hashchange',revealPortfolioEntry);
revealPortfolioEntry();
const navigation=document.querySelector('#navigation');
menuButton.addEventListener('click',()=>{const opened=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(opened));menuButton.setAttribute('aria-label',opened?'Close menu':'Open menu');navigation.classList.toggle('open',opened);});
document.addEventListener('keydown',event=>{if(event.key==='Escape'){menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','Open menu');navigation.classList.remove('open');}});
const dialog=document.querySelector('#search-dialog'),input=document.querySelector('#search-input'),results=document.querySelector('#search-results'),statusText=document.querySelector('#search-status');
results.addEventListener('click',event=>{if(event.target.closest('a'))dialog.close();});
const siteBase=new URL('.',document.querySelector('script[src$="app.js"]').src);
let indexPromise;
function getIndex(){if(!indexPromise)indexPromise=fetch(new URL('search-index.json',siteBase)).then(r=>{if(!r.ok)throw new Error('Search unavailable');return r.json();}).catch(e=>{indexPromise=null;throw e;});return indexPromise;}
document.querySelector('#search-open').addEventListener('click',()=>{dialog.showModal();input.focus();});
document.querySelector('#search-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
let searchNumber=0;
input.addEventListener('input',async()=>{const current=++searchNumber;const query=input.value.trim().toLowerCase();results.replaceChildren();if(!query){statusText.textContent='Type a topic, skill, or publication title.';return;}statusText.textContent='Searching…';try{const entries=await getIndex();if(current!==searchNumber)return;const terms=query.split(/\s+/);const hits=entries.filter(p=>terms.every(t=>(p.title+' '+p.text).toLowerCase().includes(t))).sort((a,b)=>Number(b.title.toLowerCase().includes(query))-Number(a.title.toLowerCase().includes(query)));statusText.textContent=hits.length?`${hits.length} matching ${hits.length===1?'page':'pages'}`:'No results. Try “robotics”, “PPG”, or “Python”.';for(const hit of hits){const a=document.createElement('a');a.href=new URL(hit.url.replace(/^\//,''),siteBase).href;const title=document.createElement('strong');title.textContent=hit.title+' ↗';const p=document.createElement('p');const position=hit.text.toLowerCase().indexOf(terms[0]);const start=Math.max(0,position-40);p.textContent=(start?'…':'')+hit.text.slice(start,start+160)+'…';a.append(title,p);results.append(a);}}catch{if(current===searchNumber)statusText.textContent='Search is temporarily unavailable. Please use the navigation menu.';}});
const gallery=document.querySelector('[data-gallery]');
if(gallery){const thumbnails=[...gallery.querySelectorAll('[data-src]')];let active=0;function display(n){active=(n+thumbnails.length)%thumbnails.length;const item=thumbnails[active];const img=gallery.querySelector('#gallery-image');img.src=item.dataset.src;img.alt=item.dataset.caption;gallery.querySelector('#gallery-caption').textContent=item.dataset.caption;gallery.querySelector('#gallery-count').textContent=`${active+1} / ${thumbnails.length}`;thumbnails.forEach((b,i)=>b.setAttribute('aria-pressed',String(i===active)));}thumbnails.forEach((b,i)=>b.addEventListener('click',()=>display(i)));gallery.querySelector('[data-previous]').addEventListener('click',()=>display(active-1));gallery.querySelector('[data-next]').addEventListener('click',()=>display(active+1));gallery.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();display(active-1);}if(e.key==='ArrowRight'){e.preventDefault();display(active+1);}});}
