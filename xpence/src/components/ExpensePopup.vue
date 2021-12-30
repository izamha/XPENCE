<template>
  <v-row
      align="center"
      justify="space-around" class="mt-6">
    <div class="text-center">
      <v-dialog
          v-model="dialog"
          width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
              color="orange lighten-2"
              dark
              width="150px"
              v-bind="attrs"
              v-on="on">
            Expense
          </v-btn>
        </template>
        <v-card>
          <v-card-title class="text-h5 purple--text lighten-4">
            New Expense
          </v-card-title>

          <v-card-text>
            <v-form class="px-3" ref="expenseForm">
              <v-text-field label="Amount" v-model="amount" :rules="inputRules"></v-text-field>
              <v-select
                  v-model="category"
                  :rules="inputRules"
                  :items="categories"
                  label="Category"
                  placeholder="Choose Category"></v-select>
              <v-textarea label="Description" v-model="description"></v-textarea>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text class="warning mx-0 mt-3"
                   @click="submitExpenseForm">
              Add Expense
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-row>
</template>

<script>
export default {
  name: "ExpensePopup",
  data() {
    return {
      dialog: false,
      amount: null,
      category: '',
      categories: ['Category 1', 'Category 2', 'Category 3'],
      description: '',
      inputRules: [
        v => v.length >= 3 || 'Minimum length is 5 Characters.'
      ],
    }
  },
  methods: {
    submitExpenseForm() {
      if (this.$refs.expenseForm.validate()) {
        console.log(this.amount, this.category, this.description)
      }
    }
  },
}
</script>

<style scoped>

</style>