# Write your MySQL query statement below
WITH top_students AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5
       AND AVG(course_rating) >= 4
),

course_sequence AS (
    SELECT
        cc.user_id,
        cc.course_name AS course_a,

        LEAD(cc.course_name)
        OVER (
            PARTITION BY cc.user_id
            ORDER BY cc.completion_date
        ) AS course_b

    FROM course_completions cc
    JOIN top_students ts
    ON cc.user_id = ts.user_id
)

SELECT
    course_a as first_course,
    course_b as second_course,
    COUNT(*) AS transition_count

FROM course_sequence

WHERE course_b IS NOT NULL

GROUP BY
    course_a,
    course_b

ORDER BY
    transition_count DESC,
    course_a ASC,
    course_b ASC;