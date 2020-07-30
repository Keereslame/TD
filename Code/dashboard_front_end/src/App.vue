<template>

  <div id="app">
    <b-container fluid="large">
      <!--<nav class="navbar navbar-expand navbar-dark bg-dark">
        <a href="#" class="navbar-brand">Test batch</a>
        <div class="navbar-nav mr-auto">
          <li class="nav-item">
            <a href="/batchs" class="nav-link">Batchs</a>
          </li>
          <li class="nav-item">
            <a href="/add" class="nav-link">Add</a>
          </li>
        </div>
      </nav>-->
      <div>
        <b-navbar type="dark" variant="dark">
          <b-navbar-brand class="align-center" href="/">
            <b-img width="150px" :src="require('../public/name.png')" class="logo" alt="Logo"></b-img>
          </b-navbar-brand>
        </b-navbar>
      </div>
      <!--<b-navbar-nav class="ml-auto">
        <b-nav-item href="user_settings">User settings</b-nav-item>
        <b-avatar href="profil" class="align-center"></b-avatar>
            </b-navbar-nav>-->

      <b-row>
        <b-col class="col-auto sidebar">
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
        </b-col>
        <b-col>
          <div class="container mt-3">
            <router-view />
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>


</template>

<script>
  export default {
    name: 'app'
  }
</script>


<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 0px;
  }

  .container-fluid{
    padding-right: 0px;
    padding-left: 0px;
  }
  .col-auto{
    background-color: #96d2d4;
    padding-right: 0px;
  }

  .nav-link{
    color: #2c3e50;
  }

</style>
