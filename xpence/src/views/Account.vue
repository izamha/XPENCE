<template>
  <div>
    <v-container>
      <v-row align="justify">
        <v-col cols="12" sm="4">
          <v-hover v-slot="{ hover }" open-delay="200">
            <v-card color="cyan darken-1" :elevation="hover ? 16 : 2">
              <v-row>
                <v-col cols="12" sm="8">
                  <h3>{{ account_data[0].name }}</h3>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-avatar size="100" class="ml-n10 mt-6" tile>
                    <v-img src="wallet.png"></v-img>
                  </v-avatar>
                </v-col>
              </v-row>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Account",

  mounted() {
    this.getAccount(this.account_id)
  },

  data() {
    return {
      account_id: this.$route.params.id,
      account_data: []
    }
  },

  methods: {
    getAccount(accountId) {
      axios.get(`api/account/${accountId}`)
          .then(response => {
            console.log("Successfully fetched account " + accountId)
            console.log("Account Data: ", response.data)
            this.account_data = response.data
          }).catch(error => {
        console.log("Couldn't get account ", error)
      })
    }
  }
}
</script>

<style scoped>

</style>