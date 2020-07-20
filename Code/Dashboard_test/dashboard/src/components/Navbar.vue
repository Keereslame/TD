<template>
    <div>
        <b-navbar type="dark" variant="dark">
            <b-navbar-brand class="align-center" href="#/">
                <b-img width="100px" :src="require('../../public/name.png')" class="logo" alt="Logo"></b-img>
            </b-navbar-brand>

            <b-navbar-nav class="ml-auto">
                <!--<b-nav-item href="user_settings">User settings</b-nav-item>
                <b-avatar href="profil" class="align-center"></b-avatar>-->
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "Navbar",
    }
</script>

<style scoped>

</style>