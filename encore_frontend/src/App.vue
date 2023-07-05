<style scoped>
    @font-face { font-family: Norms; src: url('/fonts/Norms/TT Norms Pro Regular.otf'); } 
    @font-face { font-family: Norms; font-weight: 500; src: url('/fonts/Norms/TT Norms Pro Bold.otf');}
    @font-face { font-family: Vastago; font-weight: 500; src: url('/fonts/Vastago/Vastago Grotesk Bold.otf');}
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
        width: 8rem;
        font-family: Norms;
        font-weight: 500;
        font-size: large;
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
        color: #A4A69C;
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
        background-color: rgba(24,31,38, .9);
        backdrop-filter: blur(10px);
        border-color: rgba(0, 0, 0, 0.2);
        border-bottom: 2px var(--bs-border-style) rgba(0, 0, 0, 0.2) !important;
    }
    .post {
        background-color: rgba(0, 0, 0, 0.2);
    }
</style>
<template>
    <div class="mb-5 fixed-top header">
    <main class="container">
        <div class="navbar mt-2 sticky-top row m-0 gap-0 pt-2 d-flex justify-content-between bg-transparent">
            <RouterLink class="navbar-brand col-2 m-0 light" to="/playlists">Navbar</RouterLink>
            <template v-if="userStore.user.isAuthenticated">
                
                <div class="col-6 m-0">
                    <div class="mb-0 pb-0 col-12">
                        <input class="form-control m-0" id="search" name="q" placeholder="Explore music" type="text">
                    </div>
                </div>
                
                <div class="col-2 m-0">
                    
                    <button @click="searchQuery" class="btn search-button align-items-center justify-content-center d-flex rounded text-center">
                    
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                        </svg>
                        
                    </button>
                </div>
                
                
                <RouterLink :to="{name: 'profile', params:{'name': userStore.user.name}}" class="col-2 m-0 d-flex justify-content-end align-items-end">
                    <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                    </svg>
                </RouterLink>
            </template>
            
            
        </div>
    </main>
    </div>
    <RouterView />
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
  beforeCreate() { 
    this.userStore.initStore()

    const token = this.userStore.user.access

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>