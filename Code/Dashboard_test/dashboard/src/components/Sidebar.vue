<template>
    <div>
        <b-nav vertical id="sidebar" >
            <b-nav-item href="/">
                <b-icon-house-door class="item"></b-icon-house-door>
            </b-nav-item>
            <b-nav-item href="/Calendar">
                <b-icon-calendar3 class="item"></b-icon-calendar3>
            </b-nav-item>
            <b-nav-item href="/Data">
                <b-icon-graph-up class="item"></b-icon-graph-up>
            </b-nav-item>
            <b-nav-item href="/Insert">
                <b-icon-file-earmark-plus class="item"></b-icon-file-earmark-plus>
            </b-nav-item>
            <b-nav-item href="/Stock">
                <b-icon-box class="item"></b-icon-box>
            </b-nav-item>
            <b-nav-item href="/Task">
                <b-icon-pencil-square class="item"></b-icon-pencil-square>
            </b-nav-item>
            <b-nav-item href="/Measure">
                <b-icon-droplet-half class="item"></b-icon-droplet-half>
            </b-nav-item>
        </b-nav>
    </div>
</template>

<script>
    export default {
        name: "Sidebar"
    }
</script>

<style scoped>
    .item{
        color: #4c5157;
        text-decoration: none;
        background-color: transparent;
        margin-bottom: 10px;
        margin-top: 10px;
        align-items: center;
    }
</style>