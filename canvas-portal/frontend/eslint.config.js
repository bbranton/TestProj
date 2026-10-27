// ESLint for the frontend: run with `npm run lint`. Prettier owns formatting,
// so eslint-config-prettier turns off any rule that would fight it.
import js from "@eslint/js";
import prettier from "eslint-config-prettier";
import reactHooks from "eslint-plugin-react-hooks";
import globals from "globals";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["dist"] },
  {
    files: ["**/*.{ts,tsx}"],
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    languageOptions: { globals: globals.browser },
    plugins: { "react-hooks": reactHooks },
    rules: {
      ...reactHooks.configs.recommended.rules,
      // Coding standards ban console.* so a Canvas token can't reach the
      // browser console.
      "no-console": "error",
    },
  },
  prettier,
);
