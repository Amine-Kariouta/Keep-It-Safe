# Keep It Safe

## English

### Description
Keep It Safe is a Chrome extension designed to filter toxicity and negativity while providing chatbot support for victims of cyberbullying. The extension uses artificial intelligence along with local APIs for improved performance and confidentiality.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amine-Kariouta/Keep-It-Safe.git
   cd Keep-It-Safe
   ```

2. **Install Python dependencies:**
   Navigate to the `api` folder and install the required packages:
   ```bash
   cd api
   pip install -r requirements.txt
   ```

3. **Load the Unpacked Extension:**
   - Navigate to `chrome://extensions/` in your Chrome browser.
   - Enable **Developer mode**.
   - Click on **Load unpacked** and select the folder containing all the files of the extension.

### Configuration for LM Studio

To set up LM Studio for this project:

- **Server Port**: Set the server port to `5002`.
- **CORS**: Enable Cross-Origin-Resource-Sharing (CORS).
- **Prompt Formatting**: Turn ON to enable prompt formatting.
- **Model**: Load the desired model in LM Studio.
- **Prompt**: Use the provided `prompt.txt` file to configure the chatbot for appropriate responses.

### Usage

1. **Start the Local Inference Server** in LM Studio:
   - Open LM Studio and set the server port to `5002`.
   - Ensure that CORS is enabled.
   - Load your preferred model and start the server.

2. **Start the APIs for Toxicity and Negativity Analysis**:
   - Run the Python script to start both APIs:
   ```bash
   python api.py
   ```

### Contact
For any questions or issues, please use the [GitHub Issues](https://github.com/AmineKariouta/keep-it-safe/issues) section.

---

## Français

### Description
Keep It Safe est une extension Chrome conçue pour filtrer la toxicité et la négativité tout en offrant un support par chatbot pour les victimes de cyberharcèlement. L'extension utilise l'intelligence artificielle ainsi que des API locales pour des performances et une confidentialité améliorées.

### Installation

1. **Clonez le repository :**
   ```bash
   git clone https://github.com/Amine-Kariouta/Keep-It-Safe.git
   cd Keep-It-Safe
   ```

2. **Installez les dépendances Python :**
   Naviguez vers le dossier `api` et installez les packages nécessaires :
   ```bash
   cd api
   pip install -r requirements.txt
   ```

3. **Chargez l'extension non empaquetée :**
   - Naviguez vers `chrome://extensions/` dans votre navigateur Chrome.
   - Activez le **mode développeur**.
   - Cliquez sur **Charger l'extension non empaquetée** et sélectionnez le dossier contenant tous les fichiers de l'extension.

### Configuration pour LM Studio

Pour configurer LM Studio pour ce projet :

- **Port du serveur** : Définissez le port du serveur sur `5002`.
- **CORS** : Activez le partage des ressources entre origines (CORS).
- **Formatage du prompt** : Activez cette option pour appliquer le formatage du prompt.
- **Modèle** : Chargez le modèle souhaité dans LM Studio.
- **Prompt** : Utilisez le fichier `prompt.txt` fourni pour configurer le chatbot afin d'obtenir des réponses appropriées.

### Utilisation

1. **Démarrez le serveur d'inférence local** dans LM Studio :
   - Ouvrez LM Studio et définissez le port du serveur sur `5002`.
   - Assurez-vous que CORS est activé.
   - Chargez votre modèle préféré et démarrez le serveur.

2. **Démarrez les APIs pour l'analyse de la toxicité et de la négativité** :
   - Exécutez le script Python pour démarrer les deux APIs :
   ```bash
   python api.py
   ```

### Contact
Pour toute question ou problème, veuillez utiliser la section [Issues GitHub](https://github.com/AmineKariouta/keep-it-safe/issues).