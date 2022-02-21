<template>
<div>
  <p>Sidebar</p>
   <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/orders">Orders</router-link>
  </nav>
<p>Sidebar end</p>
</div>
</template>

<script>
export default {
  name: "SidebarComponent"
}
</script>

<style scoped>

</style>