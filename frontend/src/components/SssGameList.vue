    <template>
  <div>
    <h1>Sss Games</h1>
    <ul>
      <li v-for="game in games" :key="game.id">
        <strong>{{ game.game }}</strong> - {{ game.price }} - {{ game.info }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      games: []
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/sss/')
      .then(response => {
        this.games =  response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
