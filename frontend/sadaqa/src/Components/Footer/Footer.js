import React from "react";

export default function Footer() {
  return (
    <div>
      <footer class="bg-dark text-light py-3 my-5">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <h4>Contact Us</h4>
              <p>
                <i class="fas fa-map-marker"></i> 123 Main Street, City, Country
              </p>
              <p>
                <i class="fas fa-phone"></i> (+20) 1155716059
              </p>
              <a>
                <i class="fas fa-envelope"></i>
                osamamagar99@gmail.com
              </a>
            </div>
            <div class="col-md-4">
              <h4>Quick Links</h4>
              <ul class="list-unstyled">
                <li>
                  <a href="#">Home</a>
                </li>
                <li>
                  <a href="#">About Us</a>
                </li>
                <li>
                  <a href="#">Services</a>
                </li>
                <li>
                  <a href="#">Contact</a>
                </li>
              </ul>
            </div>
            <div class="col-md-4">
              <h4>Follow Us</h4>
              <a href="https://facebook.com">
                <i class="fab fa-facebook"></i> 
              </a>
              <a href="https://twiter.com" className="mx-3">
                <i class="fab fa-twitter"></i> 
              </a>
              <a href="https://linkedin.com" >
                <i class="fab fa-linkedin"></i> 
              </a>

            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}