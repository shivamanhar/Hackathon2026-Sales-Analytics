class DataValidator:

    def __init__(self, df, table_name):
        self.df = df
        self.table_name = table_name

    def check_not_null(self, columns):
        results = []

        for col in columns:
            null_count = self.df.filter(f"{col} IS NULL").count()

            results.append({
                "table_name": self.table_name,
                "rule_name": f"{col}_not_null",
                "rule_type": "NOT_NULL",
                "status": "FAIL" if null_count > 0 else "PASS",
                "failed_record_count": null_count,
                "validation_timestamp": None,
            })

        return results

    def check_duplicate(self, primary_keys):
        dup_count = (
            self.df.groupBy(primary_keys)
                   .count()
                   .filter("count > 1")
                   .count()
        )

        return {
            "table_name": self.table_name,
            "rule_name": "duplicate_check",
            "rule_type": "DUPLICATE",
            "status": "FAIL" if dup_count > 0 else "PASS",
            "failed_record_count": dup_count,
            "validation_timestamp": None,
        }

    def check_row_count(self):
        row_count = self.df.count()

        return {
            "table_name": self.table_name,
            "rule_name": "row_count_check",
            "rule_type": "ROW_COUNT",
            "status": "FAIL" if row_count == 0 else "PASS",
            "failed_record_count": 0 if row_count > 0 else row_count,
            "validation_timestamp": None,
        }