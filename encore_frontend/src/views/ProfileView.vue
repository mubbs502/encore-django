<style scoped>
    @font-face { font-family: Norms; src: url('/fonts/Norms/TT Norms Pro Regular.otf'); } 
    @font-face { font-family: Norms; font-weight: 500; src: url('/fonts/Norms/TT Norms Pro Bold.otf');}
    @font-face { font-family: Vastago; font-weight: 500; src: url('public/fonts/Vastago/Vastago Grotesk Bold.otf');}
    /* Vastago Grotesk SemiBold */
    h2 {
        font-family: Vastago;
        font-weight: 500;
    }
    h3 {
        font-family: Vastago;
        font-weight: 500;
    }
    body {
        font-family: Norms;
    }
    .forgot {
        color: #A4A69C;
    }
    .radio {
        border-radius: 0.525rem;
        background-color: rgba(0, 0, 0, 0.2);
    }
    .radio-pill {
        color: #A4A69C;
        
        font-family: Norms;
        font-weight: 400;
        
    }
    .radio-pill:hover {
        color: #A4A69C;
    }
    .nav-pills {
        --bs-nav-pills-border-radius: 0.375rem;
        --bs-nav-pills-link-active-color: #A4A69C;
        --bs-nav-pills-link-active-bg: #850C01;
        --bs-nav-link-disabled-color: #A4A69C;
        box-shadow: inset 0 0px 0px rgba(0, 0, 0, 0.0), 0 0 0px rgba(0, 0, 0, 0.0);
    }
    .dark {
        background-color: #181f26;
        color: #A4A69C;
    }
    .light {
        color: #A4A69C;
    }
    .light:focus {
        color: #A4A69C;
    }
    .light:hover{
        color: #A4A69C;
    }
    .bright {
        background-color: #850C01;
        color: #A4A69C;
        font-family: Norms;
        font-weight: 500;
        font-size: large;
        border-width: 2px;
    }
    .bright:hover {
        background-color: #850C01;
        color: white;
        border-color: white;
        border-width: 2px;
    }
    .form-control:focus {
        border-color: #A4A69C;
        box-shadow: inset 0 0px 0px rgba(0, 0, 0, 0.0), 0 0 0px rgba(0, 0, 0, 0.0);
        color: #A4A69C;
        background-color: rgba(0, 0, 0, 0.2);
        border-width: 2px;
    }
    .form-control {
        background-color: rgba(0, 0, 0, 0.2);
        border-color: rgba(0, 0, 0, 0.2);
        border-width: 2px;
    }
    .form-control::placeholder {
        color: #A4A69C;
        opacity: 1;
    }
    .search-button {
        background-color: rgba(0, 0, 0, 0.2);
        color: #A4A69C;
        border-width: 2px;
        
    }
    .search-button:hover {
        background-color: rgba(0, 0, 0, 0.2);
        color: white;
        border-width: 2px;
        border-color: white;
        
    }
    .sticky-button {
        top: 5.5rem;
        
    }
    .padded {
        padding-top: 6rem;
    }
    .header {
        background-color: rgba(24,31,38, .67);
        backdrop-filter: blur(10px);
        border-color: rgba(0, 0, 0, 0.2);
        border-bottom: 2px var(--bs-border-style) rgba(0, 0, 0, 0.2) !important;
    }
    .post {
        background-color: rgba(0, 0, 0, 0.2);
    }
</style>
<template>
    <main class="container mb-5 pb-4 padded">
        <div class="" id="posts">
            <div class="row m-0 pt-4 p-0">
                <div class="">

                    <div class="">
                        <div class="row m-0 mb-4">
                            <div class="col p-0 m-0">
                                <div class="ratio ratio-1x1">
                                    <img class="border" src="https://cdn.dribbble.com/userupload/7016877/file/original-84fadcf3fd0cd7ec5f279afc78a6063e.png?compress=1&resize=1200x900" alt="" style="object-fit: cover; border-radius: 50%;">
                                </div>
                            </div>
                            
                            <div class="col-8 col-md-9 col-lg-10 d-flex justify-content-center gap-4 px-5 align-items-start flex-column">
                                <h3 class="m-0 p-0" style="font-size: x-large;">
                                    {{ userStore.user.name }}
                                </h3>
                                <button class="border btn p-2" style="width: 8rem; background-color: rgba(0, 0, 0, .2);">
                                    <p class="p-0 m-0" style="font-weight: 500; font-size: large; font-family: 'Norms';">follow</p>
                                </button>
                                
                            </div>
                        </div>
                        <br>
                        <br>
                        <div class="row m-0 mb-4 p-0 gap-4">
                                    
                                    <button class="border btn p-2" style="width: 8rem;">
                            <p class="p-0 m-0" style="font-weight: 500; font-size: large; font-family: 'Norms';">tag</p>
                        </button> 
                                
                                    <button class="border btn p-2" style="width: 8rem;">
                            <p class="p-0 m-0" style="font-weight: 500; font-size: large; font-family: 'Norms';">tag</p>
                        </button>
                                
                        </div>
                        <br>
                        <br>
                        
                        <div class="nav-scroller">
                            <ul class="nav nav-pills gap-3" id="pills-tab" role="tablist">
                                <li class="nav-item" role="presentation">
                                    <button class="nav-link radio-pill active" id="pills-playlists-tab" data-bs-toggle="pill" data-bs-target="#pills-playlists" type="button" role="tab" aria-controls="pills-playlists" aria-selected="true">My Playlists</button>
                                </li>
                                <li class="nav-item" role="presentation">
                                    <button class="nav-link radio-pill" id="pills-saved-tab" data-bs-toggle="pill" data-bs-target="#pills-saved" type="button" role="tab" aria-controls="pills-saved" aria-selected="false">My Saved Playlists</button>
                                </li>
                                <li class="nav-item" role="presentation">
                                    <button class="nav-link radio-pill" id="pills-following-tab" data-bs-toggle="pill" data-bs-target="#pills-following" type="button" role="tab" aria-controls="pills-following" aria-selected="false">Following</button>
                                </li>
                                <li class="nav-item" role="presentation">
                                    <button class="nav-link radio-pill" id="pills-followers-tab" data-bs-toggle="pill" data-bs-target="#pills-followers" type="button" role="tab" aria-controls="pills-followers" aria-selected="false">Followers</button>
                                </li>
                                <li class="nav-item" role="presentation">
                                    <button class="nav-link radio-pill" id="pills-upvoted-tab" data-bs-toggle="pill" data-bs-target="#pills-upvoted" type="button" role="tab" aria-controls="pills-upvoted" aria-selected="false">Upvoted Playlists</button>
                                </li>
                                
                            </ul>
                        </div>

                    </div>
                </div>
                
            </div>
        </div>
    </main>
    
</template>
<script>
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export default {
  setup() {
    const userStore = useUserStore()

    return {
        userStore
    }
  }, 
  
}
</script>