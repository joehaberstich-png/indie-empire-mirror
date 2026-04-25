/**
 * Fall of the Cabal — Quantum WebGL Engine v1
 * Three.js game shell with Washington DC hub
 */
(function(){
const scene=new THREE.Scene();
scene.fog=new THREE.Fog(0x0a0a0f,50,200);
scene.background=new THREE.Color(0x0a0a1a);
const camera=new THREE.PerspectiveCamera(65,window.innerWidth/window.innerHeight,0.1,1000);
const renderer=new THREE.WebGLRenderer({canvas:document.getElementById('game-canvas'),antialias:true});
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.2;
const ambient=new THREE.AmbientLight(0x222244,0.5);scene.add(ambient);
const sun=new THREE.DirectionalLight(0xff8844,1.0);sun.position.set(50,100,-50);sun.castShadow=true;sun.shadow.mapSize.width=2048;sun.shadow.mapSize.height=2048;scene.add(sun);
const fill=new THREE.DirectionalLight(0x4488ff,0.3);fill.position.set(-30,50,30);scene.add(fill);
const player=new THREE.Object3D();player.position.set(0,0,0);scene.add(player);
const cp=new THREE.Mesh(new THREE.CylinderGeometry(0.4,0.4,1.6,8),new THREE.MeshStandardMaterial({color:0xff6b35,emissive:0x441100,emissiveIntensity:0.2}));
cp.position.y=0.8;cp.castShadow=true;player.add(cp);
const ground=new THREE.Mesh(new THREE.PlaneGeometry(500,500),new THREE.MeshStandardMaterial({color:0x1a1a25,roughness:0.9,metalness:0.1}));
ground.rotation.x=-Math.PI/2;ground.receiveShadow=true;scene.add(ground);
const grid=new THREE.GridHelper(500,50,0x333355,0x222244);grid.position.y=0.05;scene.add(grid);
// Washington Monument
const m=new THREE.Mesh(new THREE.CylinderGeometry(0.5,2,40,8),new THREE.MeshStandardMaterial({color:0xddddcc,roughness:0.3,metalness:0.1}));
m.position.set(0,20,0);m.castShadow=true;scene.add(m);
// White House
const wh=new THREE.Mesh(new THREE.BoxGeometry(15,6,8),new THREE.MeshStandardMaterial({color:0xeeeeee,roughness:0.7,metalness:0.3}));
wh.position.set(-30,3,-20);wh.castShadow=true;wh.receiveShadow=true;scene.add(wh);
// Capitol
const cap=new THREE.Mesh(new THREE.BoxGeometry(20,8,12),new THREE.MeshStandardMaterial({color:0xdddddd,roughness:0.7,metalness:0.3}));
cap.position.set(40,4,10);cap.castShadow=true;cap.receiveShadow=true;scene.add(cap);
const dome=new THREE.Mesh(new THREE.SphereGeometry(4,16,8,0,Math.PI*2,0,Math.PI/2),new THREE.MeshStandardMaterial({color:0xcccccc,roughness:0.2,metalness:0.4}));
dome.position.set(40,12,10);dome.castShadow=true;scene.add(dome);
// Lincoln Memorial
const lm=new THREE.Mesh(new THREE.BoxGeometry(12,4,8),new THREE.MeshStandardMaterial({color:0xcccccc,roughness:0.7,metalness:0.3}));
lm.position.set(-20,2,40);lm.castShadow=true;lm.receiveShadow=true;scene.add(lm);
// Reflection pool
const pool=new THREE.Mesh(new THREE.PlaneGeometry(8,60),new THREE.MeshStandardMaterial({color:0x112233,transparent:true,opacity:0.6,roughness:0.1,metalness:0.5}));
pool.rotation.x=-Math.PI/2;pool.position.set(0,0.1,-30);pool.receiveShadow=true;scene.add(pool);
// Buildings
for(let i=0;i<80;i++){const x=(Math.random()-0.5)*200;const z=(Math.random()-0.5)*200;const w=3+Math.random()*8;const h=5+Math.random()*30;const d=3+Math.random()*8;const c=new THREE.Color().setHSL(0.6+Math.random()*0.1,0.1,0.1+Math.random()*0.2);const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),new THREE.MeshStandardMaterial({color:c,roughness:0.7,metalness:0.3}));b.position.set(x,h/2,z);b.castShadow=true;b.receiveShadow=true;scene.add(b);}
// Street lights
for(let x=-80;x<=80;x+=20){for(let z=-80;z<=80;z+=20){const p=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.05,2.5,4),new THREE.MeshStandardMaterial({color:0x333333}));p.position.set(x,1.25,z);scene.add(p);const l=new THREE.Mesh(new THREE.SphereGeometry(0.15,4),new THREE.MeshStandardMaterial({color:0xffaa44,emissive:0xffaa44,emissiveIntensity:0.5}));l.position.set(x,2.7,z);scene.add(l);}}
// NPCs
const npcs=[];
function npc(x,z,n,d){const o=new THREE.Mesh(new THREE.CylinderGeometry(0.3,0.3,1.6,6),new THREE.MeshStandardMaterial({color:0x44aaff,emissive:0x0044aa,emissiveIntensity:0.2}));o.position.set(x,0.8,z);o.castShadow=true;scene.add(o);o.userData={name:n,dialogue:d,type:'npc'};npcs.push(o);}
npc(-25,-15,'The Gardener','"First dead drop in Lafayette Square. Collect and report back."');
npc(35,5,'Whistleblower','"I have documents on The Circle. I need protection."');
npc(-15,35,'Informer','"Pencil Neck meeting a foreign asset at Hay-Adams. Get proof."');
// Dead drops
for(let i=0;i<5;i++){const a=Math.random()*Math.PI*2;const r=15+Math.random()*40;const d=new THREE.Mesh(new THREE.BoxGeometry(0.3,0.2,0.3),new THREE.MeshStandardMaterial({color:0x22ff88,emissive:0x00ff44,emissiveIntensity:0.5}));d.position.set(Math.cos(a)*r,0.1,Math.sin(a)*r);d.userData={type:'deaddrop',collected:false};scene.add(d);}
// Controls
const keys={};let locked=false;
document.addEventListener('keydown',e=>keys[e.code]=true);
document.addEventListener('keyup',e=>keys[e.code]=false);
document.addEventListener('mousemove',e=>{if(!locked)return;camera.rotation.y-=e.movementX*0.002;});
const cv=document.getElementById('game-canvas');
cv.addEventListener('click',()=>{if(!locked)cv.requestPointerLock();});
document.addEventListener('pointerlockchange',()=>{locked=document.pointerLockElement===cv;document.getElementById('crosshair').style.display=locked?'block':'none';});
// Game state
const g={intel:0,nfts:0,loc:'National Mall'};
function upd(){document.getElementById('player-location').textContent=`📍 ${g.loc}`;document.getElementById('player-intel').textContent=`🔍 INTEL: ${g.intel}`;document.getElementById('nft-count').textContent=`💎 NFTS: ${g.nfts}`;}
function log(m){const d=document.getElementById('mission-log');const e=document.createElement('div');e.className='entry';e.textContent=m;d.appendChild(e);d.scrollTop=d.scrollHeight;}
// Interaction
document.addEventListener('keydown',e=>{if(e.code!=='KeyE')return;const dir=new THREE.Vector3(0,0,-1).applyQuaternion(camera.quaternion);const rc=new THREE.Raycaster(camera.position,dir,0,10);const hits=rc.intersectObjects([...npcs,...scene.children.filter(c=>c.userData?.type==='deaddrop')]);if(!hits.length)return;const o=hits[0].object;if(o.userData.type==='deaddrop'&&!o.userData.collected){o.userData.collected=true;o.material.color.setHex(0x444444);g.intel+=10;g.nfts+=1;log('📄 Collected intel document +10 INTEL');upd();const nd=document.getElementById('nft-collection');nd.style.display='block';nd.innerHTML+=`<div class="item"><span>Intel Document</span><span class="rarity" style="background:#555">Normal</span></div>`;}else if(o.userData.dialogue){log(`💬 ${o.userData.name}: ${o.userData.dialogue}`);}});
// Loop
let last=0;
function anim(t){requestAnimationFrame(anim);const dt=Math.min((t-last)/1000,0.05);last=t;
npcs.forEach(n=>{n.position.y=0.8+Math.sin(t*0.002+n.position.x)*0.05;});
scene.children.forEach(c=>{if(c.userData?.type==='deaddrop'&&!c.userData.collected)c.rotation.y+=dt*2;});
const fwd=new THREE.Vector3(0,0,-1).applyQuaternion(camera.quaternion);fwd.y=0;fwd.normalize();
const rgt=new THREE.Vector3(1,0,0).applyQuaternion(camera.quaternion);rgt.y=0;rgt.normalize();
let mv=new THREE.Vector3();if(keys['KeyW'])mv.add(fwd);if(keys['KeyS'])mv.sub(fwd);if(keys['KeyA'])mv.sub(rgt);if(keys['KeyD'])mv.add(rgt);
if(mv.length()>0){mv.normalize().multiplyScalar(8*dt);player.position.add(mv);}
const dist=Math.sqrt(player.position.x**2+player.position.z**2);
if(dist<15)g.loc='Washington Monument';else if(dist<30&&player.position.z<-10)g.loc='White House';else if(player.position.z>30)g.loc='Lincoln Memorial';else g.loc='National Mall';
const co=new THREE.Vector3(0,3,6).applyAxisAngle(new THREE.Vector3(1,0,0),0.3);
const tp=player.position.clone().add(co);camera.position.lerp(tp,dt*8);camera.lookAt(player.position.x,player.position.y+1,player.position.z);
upd();renderer.render(scene,camera);}
window.addEventListener('resize',()=>{camera.aspect=window.innerWidth/window.innerHeight;camera.updateProjectionMatrix();renderer.setSize(window.innerWidth,window.innerHeight);});
setTimeout(()=>{document.getElementById('load-screen').style.opacity='0';setTimeout(()=>document.getElementById('load-screen').style.display='none',1000);},2500);
anim(0);setTimeout(()=>document.getElementById('mission-log').style.display='block',3000);
})();
