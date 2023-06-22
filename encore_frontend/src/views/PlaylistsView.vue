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
                <div class="col-lg-8">
                    <div class="vstack mb-5">
                        <img src=""/>
                        <h2>Explore</h2>
                    </div>
                    

                    <div v-for="post in posts" v-bind:key="post.id">
                        <div class="mb-1 p-3 rounded post">
                        <div class="row mb-3 m-0">
                            <h3 class="m-0 p-0 col-10">{{ post.name }}</h3>
                            <div class="d-flex col m-0 p-0 justify-content-end">
                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus-square-fill" viewBox="0 0 16 16">
                                    <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"/>
                                </svg>
                            </div>
                            
                        </div>
                        
                        
                        
                        <div class="row m-0">
                            <div class="ratio rounded ratio-1x1 border col">
                                art
                            </div>
                            <div class="col-6">
                                <ul>
                                    <li>tags</li>
                                    <li>songs</li>
                                    <li>upvotes</li>
                                    <li>{{ post.created_at_formatted }} ago</li>
                                    <li>{{ post.created_by.name }}</li>
                                    
                                </ul>
                            </div>
                            <div class="col-2 p-0 m-0 d-flex justify-content-end align-items-end">
                                <div class="">
                                    <ul>
                                        <li>--</li>
                                        <li>--</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <br>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="position-sticky col-12 sticky-button">
                        <div id="submitReset">
                            <div class="border" hidden style="height: 240px;">

                            </div>
                            <br hidden>
                            <br hidden>
                            <RouterLink to="/create" class="p-4 btn bright col-12 mb-4 rounded text-center">
                                <div class="vstack gap-2 d-flex justify-content-center  align-items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus-square-fill" viewBox="0 0 16 16">
                                        <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"/>
                                    </svg>
                                <p class="mb-0">Create playlist</p>
                                </div>
                            </RouterLink>
                            <br>
                            <br>
                            <h3>Suggested users</h3>
                            <ol>
                                <li>user 1</li>
                                <li>user 2</li>
                                <li>user 3</li>
                            </ol>
                            
                            <br>
                            <br>
                            <h3>Top playlists</h3>
                            <ol>
                                <li>user 1</li>
                                <li>user 2</li>
                                <li>user 3</li>
                            </ol>
                            <br>
                            <br>
                            <h3>Top tags</h3>
                            <ol>
                                <li>user 1</li>
                                <li>user 2</li>
                                <li>user 3</li>
                            </ol>

                        </div>
                        <br>
                    </div>
                </div>
            </div>
        </div>
    </main>
    
</template>
<script>
import axios from 'axios';

export default {
    name: 'PlaylistsView',
    data() {
        return {
            posts: []
        }
    },
    mounted() {
        this.getPlaylists()
    },
    methods: {
        getPlaylists() {
            axios
            .get('/api/posts/')
            .then(response => {
                console.log('data', response.data)

                this.posts = response.data
            })
            .catch(error => {
                console.log('error', error)
            })
        }
    }
}
</script>