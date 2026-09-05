"use strict";
const video = document.getElementById("career-video");
const chapterTitle = document.getElementById("chapter-title");
const chapterSkills = document.getElementById("chapter-skills");
const buttons = [...document.querySelectorAll("[data-time]")];
const chapters = [
  {start:0, title:"Engineering, operations, and building businesses", skills:"The experience and skills behind my work."},
  {start:1.833333, title:"Wichita State University", skills:"Team assembly · Data analysis · Academic CNC"},
  {start:12.5, title:"MKEC Engineering", skills:"AutoCAD · Revit · Trane TRACE · BIM 360"},
  {start:19.933333, title:"iTZCALi · Hard Rock · EPIC Brands", skills:"Team leadership · Hiring and training · Budget control"},
  {start:31.366667, title:"RYGNeco", skills:"Workflow design · Product requirements · Developer coordination"},
  {start:40.166667, title:"MAK Trading", skills:"Market research · Python and SQLite · AI assisted development"},
  {start:48.7, title:"Mercor", skills:"Source verification · Calculation review · Written feedback"},
  {start:58.866667, title:"Returning to engineering", skills:"UC Mechanical Engineering admission for Spring 2027"},
  {start:71.033333, title:"See the engineering work", skills:"Mechanical design · Testing · Manufacturing support"}
];
let previous = -1;
function updateChapter() {
  const time = video.currentTime;
  let index = 0;
  for (let i=1; i<chapters.length; i++) if (time>=chapters[i].start) index=i;
  if (index===previous) return;
  previous=index;
  chapterTitle.textContent=chapters[index].title;
  chapterSkills.textContent=chapters[index].skills;
  for (const button of buttons) {
    if (Math.abs(Number(button.dataset.time)-chapters[index].start)<0.01) button.setAttribute("aria-current","true");
    else button.removeAttribute("aria-current");
  }
}
for (const button of buttons) button.addEventListener("click",()=>{
  const jump=()=>{video.currentTime=Number(button.dataset.time);updateChapter();video.play().catch(()=>video.focus());};
  if(video.readyState>=1) jump();
  else {video.addEventListener("loadedmetadata",jump,{once:true});video.load();}
});
video.addEventListener("timeupdate",updateChapter);
video.addEventListener("seeked",updateChapter);
video.addEventListener("error",()=>{document.getElementById("video-error").hidden=false;});
updateChapter();
