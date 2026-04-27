SELECT
    substr(email, instr(email, '@') + 1) AS domain,
    COUNT(*) AS user_count
FROM users
GROUP BY domain
HAVING COUNT(*) >= 2
ORDER BY domain ASC;