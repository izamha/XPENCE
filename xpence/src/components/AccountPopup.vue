<template>
  <v-dialog max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon class="ml-2 mb-2" v-bind="attrs" v-on="on">
        <v-icon size="26" color="orange lighten-2">mdi-plus-circle</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title color="text-h5 purple--text lighten-4">
        <h4 class="ml-2 mt-2">New Account</h4>
      </v-card-title>
      <v-card-text>
        <v-card-subtitle>
          Create an income/expense account to start recording.
          You can create up to 5 accounts.
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
               @click="submitAccountForm">
          Add Account
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  name: "Popup",
  data() {
    return {
      id: null,
      account_name: '',
      account_currency: '',
      user: null,
      user_data: [],
      created_at: '2021-12-30T05:51:34.875789Z',
      currencies: ['Rwf', 'USD', 'USh', 'Ksh'],
      due: null,
      inputRules: [
        v => v.length >= 3 || 'Minimum length is 5 Characters.'
      ],
    }
  },

  mounted() {
    // Check current user every now and then
    axios.get("/auth/users/me")
        .then(response => {
          console.log('CurrentUser Data.', response)
          this.user_data = response.data
          this.getIncomeByUser(this.user_data['id'])
          this.submitAccountForm()
        })
        .catch(error => {
          console.log("Something went wrong. Couldn't get user. ", error)
        })
  },

  methods: {
    submitAccountForm() {
      if (this.$refs.accountForm.validate()) {
        const formData = {
          id: this.id,
          name: this.account_name,
          currency: this.account_currency,
          user: 1,
          created_at: this.created_at,
        }
        axios.post('/api/account/create/', formData)
            .then(response => {
              console.log(this.account_name, this.account_currency)
              console.log("Successfully created an Account", response.data)
            })
            .catch(error => {
              console.log("Sorry, couldn't save the Account", error)
            })
      }
    },

  },
  computed: {},
}
</script>

<style scoped>

</style>