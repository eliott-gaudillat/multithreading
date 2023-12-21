//
// Created by berni on 20/12/2023.
//
#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class Task {
 public:
  int identifier;
  int size;
  Eigen::MatrixXd matrixA;
  Eigen::VectorXd vectorB;
  Eigen::VectorXd vectorX;
  double timeExecution;

  Task(int id, int sz) : identifier(id), size(sz) {
    // Initialize other attributes as needed
  }

  void solve() {
    std::cout << "Waiting for task ... \n";
    const cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});

    if (r.status_code != 200) {
      std::cerr << "Error: No response from server\n";

    } else {
      std::cout << "Task received\n";
      auto const json_task = json::parse(r.text);
      identifier = json_task.at("identifier");
      size = json_task.at("size");

      matrixA.resize(json_task.at("a").size(), json_task.at("a")[0].size());
      for (int i = 0; i < matrixA.rows(); ++i) {
        for (int j = 0; j < matrixA.cols(); ++j) {
          matrixA(i, j) = json_task.at("a")[i][j];
        }
      }

      vectorB.resize(json_task.at("b").size());
      for (int i = 0; i < vectorB.size(); ++i) {
        vectorB(i) = json_task.at("b")[i];
      }

      auto start_time = std::chrono::high_resolution_clock::now();
      vectorX = matrixA.lu().solve(vectorB);
      auto end_time = std::chrono::high_resolution_clock::now();
      timeExecution = std::chrono::duration_cast<std::chrono::microseconds>(
                          end_time - start_time)
                          .count() /
                      1000;

      // Send back information in JSON format
      // sendBackInfo();
    }
  }

  void sendBackInfo() const {
    json json_result;
    json_result["identifier"] = identifier;
    json_result["size"] = size;

    // Convert Eigen matrix to nested std::vector
    std::vector<std::vector<double>> matrixA_vector(
        matrixA.rows(), std::vector<double>(matrixA.cols()));
    for (int i = 0; i < matrixA.rows(); ++i) {
      for (int j = 0; j < matrixA.cols(); ++j) {
        matrixA_vector[i][j] = matrixA(i, j);
      }
    }
    json_result["a"] = matrixA_vector;

    // Convert Eigen vector to std::vector
    std::vector<double> vectorB_vector(vectorB.data(),
                                       vectorB.data() + vectorB.size());
    json_result["a"] = vectorB_vector;

    // Convert Eigen vectorX to std::vector
    std::vector<double> vectorX_vector(vectorX.data(),
                                       vectorX.data() + vectorX.size());
    json_result["x"] = vectorX_vector;

    json_result["time"] = timeExecution;

    const cpr::Response r =
        cpr::Post(cpr::Url{"http://localhost:8000/"},
                  cpr::Header{{"Content-Type", "application/json"}},
                  cpr::Body{json_result.dump()});

    if (r.status_code != 200) {
      std::cerr << "Error sending back information\n";
      // Handle the error as needed
    } else {
      std::cout << "Information sent back successfully\n";
    }
  }
};

int main() {
  Eigen::setNbThreads(2);
  Task task(0, 0);
  task.solve();

  // Access the attributes of the task object as needed
  std::cout << "Task ID: " << task.identifier << "\n";
  std::cout << "Task Size: " << task.size << "\n";
  std::cout << "Execution Time: " << task.timeExecution << " ms\n";

  // ... and so on.

  return 0;
}
