## English

### Description
Keep It Safe is a Chrome extension designed to filter toxicity and negativity while providing chatbot support for victims of cyberbullying. The extension uses artificial intelligence along with local APIs for improved performance and confidentiality.

### Installation

1. **Install LM Studio**  
   Make sure LM Studio is installed on your system. You can download it from [LM Studio website](https://link-to-lm-studio).

2. **Clone the repository:**
   ```bash
   git clone https://github.com/Amine-Kariouta/Keep-It-Safe.git
   cd Keep-It-Safe
   ```

3. **Install Python dependencies:**
   Navigate to the `api` folder and install the required packages:
   ```bash
   cd api
   pip install -r requirements.txt
   ```

### Extension Installation
The extension is available on the Chrome Web Store. You can install it directly from the following link:  
[Keep It Safe on Chrome Web Store](https://chromewebstore.google.com/detail/keep-it-safe/pgaoojojkgmckjppegnpacaifghfofeo)

### Configuration for LM Studio

To set up LM Studio for this project:

- **Server Port**: Set the server port to `5002`.
- **CORS**: Enable Cross-Origin-Resource-Sharing (CORS).
- **Prompt Formatting**: Turn ON to enable prompt formatting.
- **Model and Prompt**: Load the desired model in LM Studio and use the provided `prompt.txt` file to configure the chatbot for appropriate responses.

### Usage

1. **Start the Local Inference Server** in LM Studio:
   - Start the server.

2. **Start the APIs for Toxicity and Negativity Analysis**:
   - Run the Python script to start both APIs:
   ```bash
   python api.py
   ```

### Contact
For any questions or issues, please use the [GitHub Issues](https://github.com/AmineKariouta/keep-it-safe/issues).

You can also connect with me on [LinkedIn](https://linkedin.com/in/amine-kariouta).

---

## Français

### Description
Keep It Safe est une extension Chrome conçue pour filtrer la toxicité et la négativité tout en offrant un support par chatbot pour les victimes de cyberharcèlement. L'extension utilise l'intelligence artificielle ainsi que des API locales pour des performances et une confidentialité améliorées.

### Installation

1. **Installez LM Studio**  
   Assurez-vous que LM Studio est installé sur votre système. Vous pouvez le télécharger depuis le site [LM Studio](https://link-to-lm-studio).

2. **Clonez le repository :**
   ```bash
   git clone https://github.com/Amine-Kariouta/Keep-It-Safe.git
   cd Keep-It-Safe
   ```

3. **Installez les dépendances Python :**
   Naviguez vers le dossier `api` et installez les packages nécessaires :
   ```bash
   cd api
   pip install -r requirements.txt
   ```

### Installation de l'Extension
L'extension est disponible sur le Chrome Web Store. Vous pouvez l'installer directement depuis le lien suivant :  
[Keep It Safe sur le Chrome Web Store](https://chromewebstore.google.com/detail/keep-it-safe/pgaoojojkgmckjppegnpacaifghfofeo)

### Configuration pour LM Studio

Pour configurer LM Studio pour ce projet :

- **Port du serveur** : Définissez le port du serveur sur `5002`.
- **CORS** : Activez le partage des ressources entre origines (CORS).
- **Formatage du prompt** : Activez cette option pour appliquer le formatage du prompt.
- **Modèle et Prompt** : Chargez le modèle souhaité dans LM Studio et utilisez le fichier `prompt.txt` fourni pour configurer le chatbot afin d'obtenir des réponses appropriées.

### Utilisation

1. **Démarrez le serveur d'inférence local** dans LM Studio :
   - Démarrez le serveur.

2. **Démarrez les APIs pour l'analyse de la toxicité et de la négativité** :
   - Exécutez le script Python pour démarrer les deux APIs :
   ```bash
   python api.py
   ```

### Contact
Pour toute question ou problème, veuillez utiliser la section [Issues GitHub](https://github.com/AmineKariouta/keep-it-safe/issues).

Vous pouvez également me contacter sur [LinkedIn](https://linkedin.com/in/amine-kariouta).

