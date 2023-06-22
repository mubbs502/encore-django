<style scoped>
    @font-face { font-family: Norms; src: url('/fonts/Norms/TT Norms Pro Regular.otf'); } 
    @font-face { font-family: Norms; font-weight: 500; src: url('/fonts/Norms/TT Norms Pro Bold.otf');}
    @font-face { font-family: Vastago; font-weight: 500; src: url('/fonts/Vastago/Vastago Grotesk Bold.otf');}
    
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
    .padded {
        padding-top: 6rem;
    }
    .header {
        background-color: rgba(24,31,38, .67);
        backdrop-filter: blur(10px);
        border-color: rgba(0, 0, 0, 0.2);
        border-bottom: 2px var(--bs-border-style) rgba(0, 0, 0, 0.2) !important;
    }
    .forgot {
        color: #A4A69C;
    }
    .forgot:hover {
        color: white;
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
        border-width: 0px;
    }
    .radio-pill:hover {
        color: white;
    }
    .nav-pills {
        --bs-nav-pills-border-radius: 0.375rem;
        --bs-nav-pills-link-active-bg: #850C01;
        --bs-nav-link-disabled-color: #A4A69C;
        box-shadow: inset 0 0px 0px rgba(0, 0, 0, 0.0), 0 0 0px rgba(0, 0, 0, 0.0);
        border-color: rgba(0, 0, 0, 0.2);
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
    .sticky-button {
        top: 5.5rem;
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
        box-shadow: inset 0 0px 0px rgba(0, 0, 0, 0.0), 0 0 0px rgba(0, 0, 0, 0.0);
        color: #A4A69C;
        
    }
    .form-control::placeholder {
        color: #A4A69C;
        opacity: 1;
    }
    .form {
        background-color: rgba(0, 0, 0, 0.2);
    }
</style>   
<template>
    <main class="container mb-5 padded">
        <ul class="nav nav-pills align-items-start justify-content-start d-flex" id="pills-tab" role="tablist">
            <div class="hstack p-1 radio gap-2">
                <li class="nav-item" role="presentation">
                    <div id="logIn">
                        <button class="nav-link radio-pill active btn" id="pills-login-tab" data-bs-toggle="pill" data-bs-target="#pills-login" type="button" role="tab" aria-controls="pills-login" aria-selected="true">Log In</button>
                    </div>
                </li>
                <li class="nav-item" role="presentation">
                    <div id="signUp">
                        <button class="nav-link radio-pill btn" id="pills-signup-tab" data-bs-toggle="pill" data-bs-target="#pills-signup" type="button" role="tab" aria-controls="pills-signup" aria-selected="false">Sign Up</button>
                    </div>
                </li>
            </div>
        </ul>
    </main>
    
    <div class="tab-content mb-5 pb-4" id="pills-tabContent">
        <div class="tab-pane fade container p-0 show active" id="pills-login" role="tabpanel" aria-labelledby="pills-login-tab">
            
            <main class="container mb-5">
                <form v-on:submit.prevent="submitLoginForm" class="rounded form" method="post" action='home.html' id="loginForm">
                    <div class="row m-0 pt-4 p-2">
                        <div class="col-lg-8">
                            <div class="vstack mb-5">
                                <img src=""/>
                                <h2>Log in to your account</h2>
                            </div>
                            <div class="pb-2 mb-1">
                            <h3 class="">
                                Username
                            </h3>
                            Give your username
                            </div>
                            <div class="mb-1 pb-4 col-12">
                            <input v-model="form.loginUsername" class="form-control" id="usernameLogIn" name="usernameLogIn" placeholder="Username" type="text">
                            </div>
                            <br>
                            <div class="pb-2 mb-1">
                            <h3 class="">
                                Password
                            </h3>
            
                            Give your password
            
                            </div>
                            <div class="mb-1 pb-4 col-12">
                                <input v-model="form.password" class="form-control" id="passwordLogIn" name="passwordLogIn" placeholder="Password" type="password">
                            </div>

                        </div>
                        <div class="col-lg-4">
                            <div class="position-sticky sticky-button col-12">
                                <div id="submitLogIn">
                                    <button type="submit" class="p-4 btn bright col-12 mb-4 rounded text-center">
                                        <div class="vstack gap-2 d-flex justify-content-center  align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus-square-fill" viewBox="0 0 16 16">
                                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"/>
                                            </svg>
                                        <p class="mb-0">Log in</p>
                                        </div>
                                    </button>
                                    <RouterLink class="forgot d-flex" to="/forgot">
                                        Forgot password?
                                    </RouterLink>
                                    <br>
                                    
                                </div>
   
                                
                            </div>
                        </div>
                    </div>
                </form>
            </main>
        </div>
        <div class="tab-pane container p-0 fade" id="pills-signup" role="tabpanel" aria-labelledby="pills-signup-tab">
            <main class="container mb-5">
                
                <form v-on:submit.prevent="submitForm" class="rounded form" method="post" action='home.html' id="signupForm">
                    <div class="row m-0 pt-4 p-2">
                        <div class="col-lg-8">
                            <div class="vstack mb-5">
                                <img src=""/>
                                <h2>Create your account</h2>
                            </div>
                            <div class="pb-2 mb-1">
                                <h3 class="">
                                    Username
                                </h3>
                                Give your username
                            </div>
                            <div class="mb-1 pb-4 col-12">
                                <input v-model="form.name" class="form-control" id="usernameSignUp" name="usernameSignUp" placeholder="Username" type="text">
                            </div>
                            <br>
                            <div class="pb-2 mb-1">
                                <h3 class="">
                                    Email
                                </h3>
                                Give your email
                            </div>
                            <div class="mb-1 pb-4 col-12">
                                <input  v-model="form.email" class="form-control" id="emailSignUp" name="emailSignUp" placeholder="Email" type="email">
                            </div>
                            <br>
                            <div class="pb-2 mb-1">
                                <h3 class="">
                                    Password
                                </h3>
                
                                Give your password
            
                            </div>
                            <div class="mb-1 pb-4 col-12">
                                <input v-model="form.password1" class="form-control" id="passwordSignUp1" name="passwordSignUp1" placeholder="Password" type="password">
                            </div>
                            <br>
                            <div class="pb-2 mb-1">
                                <h3 class="">
                                    Confirm Password
                                </h3>
                
                                Confirm your password
            
                            </div>
                            <div class="mb-1 pb-4 col-12">
                                <input v-model="form.password2" class="form-control" id="passwordSignUp2" name="passwordSignUp2" placeholder="Confirm password" type="password">
                            </div>
                            
                            
                        </div>
                        <div class="col-lg-4">
                            <div class="position-sticky col-12 sticky-button">
                                <div id="submitSignUp">
                                    <button type="submit" class="p-4 btn bright col-12 mb-4 rounded text-center">
                                        <div class="vstack gap-2 d-flex justify-content-center  align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus-square-fill" viewBox="0 0 16 16">
                                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"/>
                                            </svg>
                                        <p class="mb-0">Sign up</p>
                                        </div>
                                    </button>
                                    <br>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </form>
            </main>
            
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    }, 
    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',
                loginUsername: '',
                password: '',
            },
            errors: [],
            signUpSuccess: false,
        }
    },
    methods: {
        async submitForm() {
            document.getElementById('submitSignUp').innerHTML = `
            <button type="submit" disabled class="p-4 btn bright col-12 mb-3 rounded text-center">
                <div class="vstack gap-2 d-flex justify-content-center  align-items-center">
                    <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                    </div>
                    <p class="mb-0">Sign up</p>
                </div>
            </button>`
            document.getElementById('logIn').innerHTML = `
            <button class="nav-link radio-pill" disabled id="pills-saved-tab" data-bs-toggle="pill" data-bs-target="#pills-saved" type="button" role="tab" aria-controls="pills-saved" aria-selected="false">Log In</button>`
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('Your username is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password2 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password2 !== this.form.password1) {
                this.errors.push('Your passwords do not match')
            }

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.errors.length === 0) {
                await axios
                .post('/api/signup/', this.form)
                .then(response => {
                    if (response.data.message === 'success') {
                        // show toast
                        console.log('sign up success')
                        this.form.loginUsername = this.form.name
                        this.form.password = this.form.password2
                        this.submitLoginForm()
                    } else {
                        // something went wrong
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })

               
            }
        },

        async submitLoginForm() {
            document.getElementById('submitLogIn').innerHTML = `
            <button type="submit" disabled class="p-4 btn bright col-12 mb-4 rounded text-center">
                <div class="vstack gap-2 d-flex justify-content-center  align-items-center">
                    <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                    </div>
                    <p class="mb-0">Log in</p>
                </div>
            </button>
            <RouterLink class="forgot d-flex" to="/forgot">Forgot password?</RouterLink><br>`
            document.getElementById('signUp').innerHTML = `
            <button class="nav-link radio-pill" disabled id="pills-saved-tab" data-bs-toggle="pill" data-bs-target="#pills-saved" type="button" role="tab" aria-controls="pills-saved" aria-selected="false">Sign Up</button>`
            this.errors = [] 

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.loginUsername === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.errors.length === 0) {
                let form = { name: this.form.loginUsername, password: this.form.password }
                await axios
                .post('/api/login/', form)
                .then(response => {
                    this.userStore.setToken(response.data)
                    console.log(response.data.access)
                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
                })
                .catch(error => {
                    console.log('error', error)
                })

                await axios
                .get('/api/me/')
                .then(response => {
                    console.log(response.data)
                    this.userStore.setUserInfo(response.data)

                    this.$router.push('/playlists')
                    
                })
                .catch(error => {
                    console.log('error', error)
                })
            }
        }
    }
}
</script>
