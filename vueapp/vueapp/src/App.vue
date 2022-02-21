<template>
  <v-app id="inspire">
    <SidebarComponent></SidebarComponent>
    <HeaderComponent></HeaderComponent>

 <v-main style="background: #f5f5f540">
      <v-container class="py-8 px-6" fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>

</template>


<script>
import SidebarComponent from "@/components/SidebarView";
import HeaderComponent from "@/components/HeaderView";

export default {
  name: "App",
  components: {HeaderComponent, SidebarComponent}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>