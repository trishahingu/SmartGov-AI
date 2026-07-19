// ===========================================
// SmartGov AI
// app.js
// Final Production Version
// ===========================================

document.addEventListener("DOMContentLoaded", () => {

    "use strict";

    /*====================================================
        ELEMENTS
    ====================================================*/

    const navbar = document.querySelector(".navbar");
    const backToTop = document.getElementById("backToTop");
    const verifyBtn = document.querySelector(".btn-warning");
    const fileInputs = document.querySelectorAll("input[type='file']");
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-link");
    const counters = document.querySelectorAll(".counter");

    /*====================================================
        NAVBAR
    ====================================================*/

    function navbarScroll() {

        if (!navbar) return;

        if (window.scrollY > 40) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    }

    navbarScroll();

    window.addEventListener("scroll", navbarScroll);

    /*====================================================
        BACK TO TOP
    ====================================================*/

    function toggleBackToTop() {

        if (!backToTop) return;

        if (window.scrollY > 350) {

            backToTop.style.display = "flex";

        } else {

            backToTop.style.display = "none";

        }

    }

    toggleBackToTop();

    window.addEventListener("scroll", toggleBackToTop);

    if (backToTop) {

        backToTop.addEventListener("click", () => {

            window.scrollTo({

                top: 0,
                behavior: "smooth"

            });

        });

    }

    /*====================================================
        SMOOTH SCROLL
    ====================================================*/

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth",
                block: "start"

            });

        });

    });

    /*====================================================
        ACTIVE NAVIGATION
    ====================================================*/

    function activateMenu() {

        let current = "";

        sections.forEach(section => {

            const top = section.offsetTop - 120;

            const height = section.clientHeight;

            if (window.scrollY >= top && window.scrollY < top + height) {

                current = section.getAttribute("id");

            }

        });

        navLinks.forEach(link => {

            link.classList.remove("active");

            if (link.getAttribute("href") === "#" + current) {

                link.classList.add("active");

            }

        });

    }

    activateMenu();

    window.addEventListener("scroll", activateMenu);

    /*====================================================
        COUNTER ANIMATION
    ====================================================*/

    const counterObserver = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (!entry.isIntersecting) return;

            const counter = entry.target;

            const target = Number(counter.dataset.target);

            let count = 0;

            const speed = target / 120;

            function updateCounter() {

                count += speed;

                if (count < target) {

                    counter.innerHTML =
                        Math.ceil(count).toLocaleString();

                    requestAnimationFrame(updateCounter);

                } else {

                    counter.innerHTML =
                        target.toLocaleString();

                }

            }

            updateCounter();

            counterObserver.unobserve(counter);

        });

    }, {

        threshold: 0.6

    });

    counters.forEach(counter => {

        counterObserver.observe(counter);

    });

    /*====================================================
        FADE ANIMATION
    ====================================================*/

    const fadeObserver = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {

        threshold: 0.2

    });

    document.querySelectorAll(".fade-up").forEach(item => {

        fadeObserver.observe(item);

    });

    /*====================================================
        BUTTON RIPPLE
    ====================================================*/

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("click", function (e) {

            const ripple = document.createElement("span");

            const size = Math.max(

                this.clientWidth,
                this.clientHeight

            );

            ripple.style.width = size + "px";
            ripple.style.height = size + "px";

            ripple.style.left =
                e.offsetX - size / 2 + "px";

            ripple.style.top =
                e.offsetY - size / 2 + "px";

            ripple.className = "ripple";

            const oldRipple =
                this.querySelector(".ripple");

            if (oldRipple) {

                oldRipple.remove();

            }

            this.appendChild(ripple);

        });

    });
        /*====================================================
        FILE INPUT PREVIEW
    ====================================================*/

    fileInputs.forEach(input => {

        input.addEventListener("change", function () {

            if (!this.files.length) return;

            this.title = this.files[0].name;

            const label = this.parentElement.querySelector(".file-name");

            if (label) {

                label.innerHTML = this.files[0].name;

            }

        });

    });

    /*====================================================
        VERIFY BUTTON LOADING
    ====================================================*/

    if (verifyBtn) {

        verifyBtn.addEventListener("click", function () {

            if (this.classList.contains("loading")) return;

            this.classList.add("loading");

            const originalText = this.innerHTML;

            this.disabled = true;

            this.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2"></span>
                Verifying Document...
            `;

            setTimeout(() => {

                this.disabled = false;

                this.classList.remove("loading");

                this.innerHTML = originalText;

            },3000);

        });

    }

    /*====================================================
        HERO TYPING EFFECT
    ====================================================*/

    const typingTitle = document.getElementById("typing-title");

    if (typingTitle) {

        const text =
        "AI Powered Government Citizen Service Portal";

        let index = 0;

        function typingEffect() {

            if(index < text.length){

                typingTitle.innerHTML += text.charAt(index);

                index++;

                setTimeout(typingEffect,40);

            }

        }

        typingEffect();

    }

    /*====================================================
        LIVE CLOCK
    ====================================================*/

    const clock = document.getElementById("clock");

    if(clock){

        function updateClock(){

            const date = new Date();

            clock.innerHTML =

            date.toLocaleDateString("en-IN") +

            " | " +

            date.toLocaleTimeString("en-IN");

        }

        updateClock();

        setInterval(updateClock,1000);

    }

    /*====================================================
        TRUST SCORE
    ====================================================*/

    const trustScore = document.getElementById("trustScore");

    if(trustScore){

        let value = 0;

        const trustInterval = setInterval(()=>{

            value++;

            trustScore.innerHTML = value + "%";

            if(value>=99){

                clearInterval(trustInterval);

            }

        },25);

    }

    /*====================================================
        PAGE LOADER
    ====================================================*/

    const loader = document.getElementById("loader");

    if(loader){

        window.addEventListener("load",()=>{

            setTimeout(()=>{

                loader.classList.add("loader-hide");

            },800);

        });

    }

    /*====================================================
        WELCOME POPUP
    ====================================================*/

    const popup = document.getElementById("welcomePopup");

    window.closePopup = function(){

        if(popup){

            popup.classList.add("hidePopup");

        }

    }

    /*====================================================
        TOAST MESSAGE
    ====================================================*/

    const toast = document.getElementById("toast");

    if(toast){

        setTimeout(()=>{

            toast.style.display="block";

            toast.style.opacity="1";

        },2500);

        setTimeout(()=>{

            toast.style.opacity="0";

            setTimeout(()=>{

                toast.style.display="none";

            },400);

        },6500);

    }

    /*====================================================
        PARTICLE BACKGROUND
    ====================================================*/

    const particleContainer = document.getElementById("particles");

    if(particleContainer){

        for(let i=0;i<40;i++){

            const particle = document.createElement("span");

            particle.className="particle";

            particle.style.left=Math.random()*100+"%";

            particle.style.animationDuration=

            (5+Math.random()*8)+"s";

            particle.style.animationDelay=

            Math.random()*5+"s";

            particleContainer.appendChild(particle);

        }

    }

    /*====================================================
        INITIALIZE
    ====================================================*/

    console.log(

        "%c SmartGov AI Loaded Successfully",

        "color:#0B5ED7;font-size:14px;font-weight:bold;"

    );

});
