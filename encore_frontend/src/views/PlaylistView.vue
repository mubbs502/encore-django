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
        background-color: #181f26;
        border-width: 2px;
    }
    .form-control {
        background-color: #181f26;
        border-color: #181f26;
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
        {{ playlist.name }}
    </main>
    
</template>
<script>
import axios from 'axios';

export default {
    name: 'PlaylistView',
    data() {
        return {
            playlist: {}
        }
    },

    async beforeMount() {
        const paramName = this.$router.currentRoute.value.params.name
        await this.getPlaylist(paramName)
    },
    
    methods: {
        
        async getPlaylist(name) {
            await axios
            .get('/api/posts/retrieve/' + name)
            .then(response => {
                console.log('data', response.data)
                
                this.playlist = response.data
                
            })
            .catch(error => {
                console.log('error', error)
            })

        }

    }
}
</script>