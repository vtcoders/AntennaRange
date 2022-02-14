
                var slideIndex = 0;
                showSlidesAuto();

                function showSlidesAuto()
                {
                    plusSlides(1);
                    setTimeout(showSlidesAuto, 10000);
                }

                // Next/previous controls
                function plusSlides(n) {
                showSlides(slideIndex += n);
                }

                // Thumbnail image controls
                function currentSlide(n) {
                showSlides(slideIndex = n);
                }

                function showSlides(n) {
                var i;
                var slides = document.getElementsByClassName("mySlides");
                var dots = document.getElementsByClassName("dot");
                if (n > slides.length) {slideIndex = 1}
                if (n < 1) {slideIndex = slides.length}
                for (i = 0; i < slides.length; i++) {
                    slides[i].style.display = "none";
                }
                for (i = 0; i < dots.length; i++) {
                    dots[i].className = dots[i].className.replace(" dotActive", "");
                }
                slides[slideIndex-1].style.display = "block";
                dots[slideIndex-1].className += " dotActive";
                } 
