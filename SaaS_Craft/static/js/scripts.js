const allArticle = document.querySelector(".all_article");
const backBtn = document.getElementById("backBtn");
const nextBtn = document.querySelector("#nextBtn");


backBtn.addEventListener("click", ()=>{
    allArticle.scrollLeft -= 500;
    allArticle.style.scrolBehavior = "smooth";
})


nextBtn.addEventListener('click', ()=>{
    allArticle.scrollLeft += 500;
    allArticle.style.scrolBehavior = "smooth"
})