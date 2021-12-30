<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="4">
          <!-- Income vs Expense Card -->
          <income-vs-expense></income-vs-expense>

          <!-- Income Popup -->
          <v-row>
            <v-col class="mx-0">
              <income-popup></income-popup>
            </v-col>
            <!-- Expense Popup -->
            <v-col class="mx-0">
              <expense-popup></expense-popup>
            </v-col>
          </v-row>

          <v-row justify="space-around" class="mt-8">
            <v-sheet class="stackSheet" color="white">
              <v-sparkline
                  :value="value1"
                  color="deep-purple"
                  :line-width="width"
                  :smooth="radius || false"
                  :padding="padding"
                  :margin="margin"
              ></v-sparkline>
              <v-sparkline
                  class="stackSpark"
                  :value="value2"
                  :smooth="radius || false"
                  color="orange"
                  :line-width="width"
                  :padding="padding"></v-sparkline>
            </v-sheet>
          </v-row>

          <v-row justify="space-around" class="mt-8">
            <v-card color="orange-light" elevation="2">
              <v-card-title>
                Income Vs Expenses
              </v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <div>
                  <apexchart
                      width="350" type="donut"
                      :options="options" :series="series" :labels="labels">
                  </apexchart>
                </div>
              </v-card-text>
            </v-card>
          </v-row>

        </v-col>
        <v-col cols="12" sm="1">
          <v-divider vertical></v-divider>
        </v-col>
        <v-col cols="12" sm="7">
            <div class="column_wrapper">
              <!-- results of <div v-for="item in list"></div>  -->
              <div>Item 1 Item 1</div>
              <div>Item 2</div>
              <div>Item 3</div>
              <div>Item 4</div>
              <div>Item 5</div>
              <div>Item 6</div>
              <div>Item 7</div>
              <div>Item 8</div>
              <div>Item 9</div>
              <div>Item 10</div>
              <div>Item 11</div>
              <div>Item 12</div>
              <div>Item 13</div>
              <div>Item 14</div>
              <div>Item 15</div>
            </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

import axios from "axios";
import IncomePopup from "@/components/IncomePopup";
import ExpensePopup from "@/components/ExpensePopup";
import IncomeVsExpense from "@/components/IncomeVsExpense";

export default {
  name: 'Home',
  components: {
    IncomePopup,
    ExpensePopup,
    IncomeVsExpense,
  },

  data: () => ({
        tab: null,
        text: 'center',
        fill: true,
        margin: true,
        padding: 8,
        radius: 10,
        value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
        width: 2,
        lineCap: 'round',
        autoLineWidth: false,
        fills: false,

        date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        menu: false,
        modal: false,
        menu2: false,

        user_data: [],
        test: [],

        series: [44, 55, 41, 17, 15],
        options: {
          labels: ['Shoes', 'Pricey Shirt', 'Internet', 'Travels', 'Groceries'],
          chart: {
            type: 'donut',
          },
          responsive: [{
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: 'bottom'
              }
            }
          }]
        },

        value1: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
        value2: [7, 4, 7, 2, 9, 0, 1, 2, 4, 7, 7, 10, 1, 3, 5],

        itemsPerPageArray: [4, 8, 12],
        search: '',
        filter: {},
        sortDesc: false,
        page: 1,
        itemsPerPage: 4,
        sortBy: 'name',
        keys: [
          'Name',
          'Song',
          'Album',
        ],
        items: [
          {
            name: 'Frozen Yogurt',
            song: 'My Heart Will Go On',
            album: 'Lonely Keyboard',
          },
        ],

        total_income: [],
        total: null,

      }
  ),

  mounted() {
    axios.get("/auth/users/me")
        .then(response => {
          console.log('CurrentUser Data.', response)
          this.user_data = response.data
          this.getIncomeByUser(this.user_data['id'])
        })
        .catch(error => {
          console.log("Couldn't get current user: ", error)
        })
  }
  ,
  methods: {
    getIncomeByUser(userId) {
      axios.get(`/api/income/by/${userId}`)
          .then(response => {
            this.total_income = response.data
            let total = 0
            for (let i = 0; i <= this.total_income.length; i++) {
              total += this.total_income[i].amount
              console.log("Income of user ( " + userId + ")", total)
              this.total = total
            }
          }).catch(error => {
        console.log("Couldn't get this user's Income", error)
      })
    }
  },

  computed: {
    numberOfPages() {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
    filteredKeys() {
      return this.keys.filter(key => key !== 'Name')
    },
  }

}
</script>

<style scoped lang="sass">
.v-card.on-hover.theme--dark
  background-color: rgba(#ffffff, 0.8)

  > .v-card__text
    color: #000
</style>

<style lang="css" scoped>
.border {
  border-right: 1px solid grey;
}

.stackSheet {
  position: relative;
}

.stackSpark {
  position: absolute;
  top: 0;
  left: 0;
}

.column_wrapper {
  column-count: 5;
}

</style>
