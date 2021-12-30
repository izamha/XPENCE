<template>
  <div id="app">
    <v-app id="expence">
      <div>
        <v-app-bar
            color="light lighten-4"
            dense clipped-left>

            <v-img alt="Expence Logo"
                   class="mx-2"
                   max-height="40"
                   max-width="40"
                   contain
                   :src="require('@/assets/logo.png')"></v-img>

          <v-toolbar-title>Page title</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-menu
              left
              bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-avatar size="40">
                <v-img alt="Expence Logo"
                       class="shrink mr-2"
                       contain :src="require('@/assets/logo.png')"></v-img>
              </v-avatar>
              <v-btn
                  icon
                  v-bind="attrs"
                  v-on="on">
                <v-icon>mdi-drop-down</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                  v-for="n in 5"
                  :key="n"
                  @click="() => {}"
              >
                <v-list-item-title>Option {{ n }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-app-bar>
      </div>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>
a {
  color: #fff3cd;
}
</style>