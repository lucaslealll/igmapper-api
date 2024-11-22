/**
 * A função getCookie() analisa os cookies presentes na página atual e os organiza em um objeto chave-valor.
 * Cada cookie é separado por ponto e vírgula (;) no documento de cookies.
 * A função retorna um objeto contendo todos os cookies, onde as chaves são os nomes dos cookies
 * e os valores são os respectivos valores dos cookies.
 * 
 * @returns {Object} Um objeto contendo todos os cookies da página, organizados como chave-valor.
 */
function getCookie() {
    const cookies = document.cookie.split(';');
    const cookieObj = {};
    cookies.forEach(cookie => {
        const [name, value] = cookie.split('=').map(c => c.trim());
        cookieObj[name] = value;
    });
    return cookieObj;
}
return getCookie();