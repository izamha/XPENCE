<template>
  <v-dialog max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-list nav dense>
        <v-list-item-group v-model="selectedItemInDrawer">
          <v-list-item>
            <v-list-item-icon>
              <v-icon small>fas fa-cog</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Preferences</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon small>fas fa-user</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-bind="attrs" v-on="on">My Profile</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-divider class="mt-12 mb-6"></v-divider>
        <v-spacer></v-spacer>
        <v-list-item-group class="mt-6" color="deep-purple">
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon>mdi-chevron-right</v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </template>
    <v-card>
      <v-card-title color="text-h5 purple--text lighten-4">
        <h4 class="ml-2 mt-2">My Profile Info</h4>
      </v-card-title>
      <v-card-text>
        <v-card-subtitle>
        </v-card-subtitle>
        <v-form class="px-3" ref="accountForm">
          <v-text-field label="Name" v-model="account_name" :rules="inputRules"></v-text-field>
          <v-select
              v-model="account_currency"
              :rules="inputRules"
              :items="currencies"
              label="Currency"
              placeholder="Choose Currency"
          ></v-select>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text class="warning mx-0 mt-3"
               @click="submitProfileForm">
          Save Profile
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ProfilePopup",
  data() {
    return {
      dialog: false,
      selectedItemInDrawer: 0,
      drawerItems: [
        {icon: 'fas fa-cog', text: 'Preferences', route: '/preferences'},
        {icon: 'fas fa-user', text: 'My Profile', route: '/profile'},
      ],
    }
  },
  methods: {
    submitProfileForm() {}
  }
}
</script>

<style scoped>

</style>